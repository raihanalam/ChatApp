from pyexpat import model
from django import forms
from .models import ChatRoom

class NewRoom(forms.ModelForm):
     class Meta:
          model = ChatRoom
          exclude = ('users')