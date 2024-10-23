from django.db import models
from django.contrib.auth.models import User
from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    String,
    Integer,
    Float,
    insert,
    inspect,
    text
)
# Create your models here.
class Chat(models.Model):
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self}: {self.message}'


class receipt(models.Model):
    client_name = models.TextField()
    price = models.IntegerField()
    phone = models.TextField()
    profession = models.TextField()
    location = models.TextField()

