from django.shortcuts import render, HttpResponseRedirect
from .forms import CreateNewUser, SigninForm, ProfilePic
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth.forms import PasswordChangeForm


def sign_up(request):
     my_form = CreateNewUser()
     registerd = False

     if request.method == 'POST':
          my_form = CreateNewUser(data=request.POST)
          if my_form.is_valid():
               user = my_form.save()
               registerd = True
               try:
                    user_profile = UserProfile(user=user)
                    user_profile.save()
                    messages.success(request,"Yor account has been created.")
                    return HttpResponseRedirect(reverse('account:sign_in'))
               except:
                    messages.warning(request,"There is a problem creting in your accont. Please check and try again!")
               return HttpResponseRedirect(reverse('account:sign_in'))

     return render(request,'signup.html',context={'form':my_form,'registerd':registerd})

def sign_in(request):
     form = SigninForm()
     if request.method == "POST":
          form = SigninForm(data=request.POST)
          if form.is_valid():
               username = form.cleaned_data.get('username')
               password = form.cleaned_data.get('password')
               user = authenticate(username=username,password=password)
               if user is not None:
                    login(request,user)
                    return HttpResponseRedirect(reverse('chat:home'))
               
     return render(request,'signin.html',context={'form':form})

@login_required
def sign_out(request):
     logout(request)
     return HttpResponseRedirect(reverse('account:sign_in'))


@login_required
def change_password(request):
     current_user = request.user
     form = PasswordChangeForm(current_user)

     if request.method == "POST":
          form = PasswordChangeForm(current_user,data = request.POST)
          if form.is_valid():
               form.save()

     return render(request,'change_password.html',context={'form':form})

@login_required
def add_pro_pic(request):
     form = ProfilePic()

     if request.method == "POST":

          form = ProfilePic(request.POST,request.FILES)

          if form.is_valid():
               user_obj = form.save(commit=False)

               user_obj.user = request.user
               user_obj.save() #commit true default
               return HttpResponseRedirect(reverse('chat:profile'))

     return render(request,'change_pro_pic.html',context={'form': form})


@login_required
def change_pro_pic(request):
     form = ProfilePic(instance=request.user.user_profile)
     if request.method == "POST":
          form = ProfilePic(request.POST,request.FILES,instance=request.user.user_profile)
          if form.is_valid():
               form.save()
               return HttpResponseRedirect(reverse('chat:profile'))

     return render(request,'change_pro_pic.html',context={'form': form})