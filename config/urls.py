"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView # new
import whitenoise

urlpatterns = [
    path('Home', TemplateView.as_view(template_name='aboutme.html'), name='Oelkuct'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('WEBDEV', TemplateView.as_view(template_name='WEBDEV.html'), name='Web Dev'),
    path('DS', TemplateView.as_view(template_name='DS.html'), name='Data Science'),
    path('SWE', TemplateView.as_view(template_name='SWE.html'), name='SWE'),
    path('FSE', TemplateView.as_view(template_name='FSE.html'), name='FULLSTACK'),

    path('FSE/Alerts', TemplateView.as_view(template_name='Text Alerts and Monitoring.html'), name = 'Alerts'),
    path('FSE/CNN', TemplateView.as_view(template_name='CNN Classification.html'), name='CNN'),
    path('FSE/ERP', TemplateView.as_view(template_name='ERP Page.html'), name='ERP'),
    path('chatbot/', include('ragoo.urls')),
    path('FSE/survey-breaker-llm', TemplateView.as_view(template_name='survey_breaker_LLM.html'), name='Survey Breaker LLM'),


]
