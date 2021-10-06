from django.db import models

class User(models.Model):
    user_login = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    user_surname = models.CharField(max_length=50)

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=200)
    task_time = models.DateField()
    task_status = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
