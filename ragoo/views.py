from django.shortcuts import render, redirect
from django.http import JsonResponse

from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat

from django.utils import timezone
from transformers.agents import Tool
from transformers.agents import ReactCodeAgent, HfEngine
from huggingface_hub import login
from django.db import connection
from huggingface_hub import login
from django.contrib.auth.decorators import login_required
import os
import huggingface_hub
from pathlib import Path
hf_token = os.environ.get('HF_TOKEN')
huggingface_hub.login(hf_token)
cursor = connection.cursor()


class SQLExecutorTool(Tool):
    name = "sql_engine"
    columns_info = [('client_name', 'VARCHAR(length=50)'), ('price',  'FLOAT())'), ('profession',  'VARCHAR(length=50)'), ('phone', 'VARCHAR(length=50)'), ('location', 'VARCHAR(length = 50)')]
    table_description = "Columns:\n" + "\n".join([f"  - {name}: {col_type}" for name, col_type in columns_info])
    description = f"""Allows you to perform SQL queries on the table. Returns a string representation of the result. Always answer in Full sentences.
The table is named 'ragoo_receipt'. Its description is as follows: \n{table_description}"""
    inputs = {
        "query": {
            "type": "text",
            "description": f"The query to perform. This should be correct SQL. Always answer in Full sentences",
        }
    }
    output_type = "text"

    def forward(self, query: str) -> str:
        output = ""
        with connection.cursor() as con:
            print(query.lower())
            con.execute(str(query.lower()))
            rows = con.fetchall()
            for row in rows:
                output += "\n" + str(row)
        return output

def ask_openai(message):
    agent = ReactCodeAgent(
        tools=[SQLExecutorTool()],
        llm_engine=HfEngine("meta-llama/Meta-Llama-3-70B-Instruct"),

    )
    answer = agent.run(message.lower())
    return answer

# Create your views here.
def chatbot(request):
    chats = Chat.objects.all()

    if request.method == 'POST':
        message = request.POST.get('message')
        message = message.lower()
        response = ask_openai(message.lower())

        chat = Chat(message=message, response=response, created_at=timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'ragoo.html', {'chats': chats})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('chatbot')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('chatbot')
            except:
                error_message = 'Error creating account'
                return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = 'Password dont match'
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
