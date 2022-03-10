from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile


class CreateNewUser(UserCreationForm):
     email = forms.EmailField(required=True,label="",widget=forms.TextInput(attrs={'placeholder':'Email'}))
     username = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'placeholder':'Username'}))
     password1 = forms.CharField(required=True,label="",widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
     password2 = forms.CharField(required=True,label="",widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
     
     class Meta:
          model = User
          fields = ('email','username','password1','password2')

class SigninForm(AuthenticationForm):
     username = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'placeholder':'Username'}))
     password = forms.CharField(required=True,label="",widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
     
     class Meta:
          model = User
          fields = ('username','password')

class EditProfile(forms.ModelForm):
     class Meta:
          dob = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
          model = UserProfile
          exclude = ('user',)

class UserProfileChange(UserChangeForm):
     email = forms.EmailField(required=True,label="",widget=forms.TextInput(attrs={'placeholder':'Email'}))
     username = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'placeholder':'Username'}))
     first_name = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'placeholder':'First Name'}))
     last_name = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
     password = None
     """password = forms.CharField(required=True,label="",widget=forms.PasswordInput(attrs={'placeholder':'Password'}))"""

     class Meta:
          model = User
          fields = ('username','email','first_name','last_name')

class ProfilePic(forms.ModelForm):
     class Meta:
          model = UserProfile
          fields = ['profile_pic',]

