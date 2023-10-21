from django.db import models
from django.contrib.auth.models import User

class Accounts(models.Model):
    account = models.AutoField(primary_key=True)
    program_name = models.CharField(max_length=250)
    email = models.EmailField(null=True)
    username = models.CharField(max_length=150, null=True)
    description = models.TextField(max_length=400, null=True)
    password = models.CharField(max_length=150)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

class Passwords(models.Model):
    password_key = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    password = models.CharField(max_length=200)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
