from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Message(models.Model):
 message = models.CharField(max_length=200)
 created_on = models.DateTimeField()
 updated_on = models.DateTimeField()
 created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message') 

 def __str__(self):
  return self.message  


@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance = None, created = False,**kwargs):
  if created:
    Token.objects.create(user=instance)