from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class ChatRoom(models.Model):
     name = models.CharField(max_length=255,unique=True, blank=False)
     users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, help_text="users who are connected to the chat")
     mode = models.BooleanField(default=False)
     key = models.CharField(max_length=100,unique=True,blank=True)

     def __str__(self):
          return self.name

     def connect_user(self, user):
          """
          return true if user is added to the users list
          """
          is_user_added = False
          if not user in self.users.all():
               self.users.add(user)
               self.save()
               is_user_added = True
          elif user in self.users.all():
               is_user_added = True
          return is_user_added

     def disconnect_user(self, user):
          """
          return true if user is removed to the users list
          """
          is_user_removed = False
          if user in self.users.all():
               self.users.remove(user)
               self.save()
               is_user_removed = True
          return is_user_removed


class Chat(models.Model):
     content = models.CharField(max_length=1000)
     timestamp = models.DateTimeField(auto_now_add=True)
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     room = models.ForeignKey(ChatRoom, on_delete= models.CASCADE)

