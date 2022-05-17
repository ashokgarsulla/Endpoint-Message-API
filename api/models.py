import email
from turtle import mode
from django.db import models

class User(models.Model):
 name = models.CharField(max_length=50)
 email = models.EmailField(max_length=50)

 def __str__(self):
  return self.name


class Message(models.Model):
 message = models.CharField(max_length=200)
 created_on = models.DateTimeField()
 updated_on = models.DateTimeField()
 created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message') 

 def __str__(self):
  return self.message