from email import message
from sre_constants import SUCCESS
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.models import User
from django.views import View
from django.views.generic import CreateView, TemplateView

from account.forms import UserProfileChange
from .models import Chat, ChatRoom
import shortuuid
import re
from datetime import datetime
from django.urls import reverse


# Create your views here.
class Home(LoginRequiredMixin, View):
     def get(self, request,):
          c_user = request.user
          user_rooms = ChatRoom.objects.filter(users__username=c_user)

          return render(request, 'home.html', context={'user_rooms':user_rooms})

class Profile(LoginRequiredMixin,TemplateView):
     def get(self, request):
          c_user = request.user
          form = UserProfileChange(instance = c_user)
          user_data = User.objects.get(username=c_user)
          
          return render(request,'profile.html',context={'user':user_data,'form':form})

     def post(self,request):
          c_user = request.user
          form = UserProfileChange(request.POST, instance = c_user)

          if form.is_valid():
               form.save()
               form = UserProfileChange(instance=c_user)
          return render(request,'profile.html',context={'form':form})



class Room(LoginRequiredMixin, View):

     def get(self, request, room_name):
          c_user = request.user
          user_room = True

          room = ChatRoom.objects.filter(name=room_name,users__username=c_user).first()

          chats = []

          if room:
               chats = Chat.objects.filter(room=room)
               return render(request, 'chatroom.html', context={'room_name':room_name, 'current_room':room, 'chats':chats})
          else:
               #room = ChatRoom(name=room_name)
               #room.save()
               user_room = False
               messages.warning(request,f"You are not added to {room_name} box!")
               return HttpResponseRedirect(reverse('chat:home'))

          #return render(request, 'chatroom.html', context={'room_name':room_name, 'chats':chats})

class Inbox(LoginRequiredMixin, View):

     def get(self, request):
          c_user = request.user
          my_rooms = ChatRoom.objects.filter(users__username=c_user)

          return render(request, 'inbox.html', context={'my_rooms':my_rooms})

     def post(self, request, *args, **kwargs):
          c_user = request.user
          mode = request.POST['mode']
          name = request.POST['name']

          name_check = False
          blank_name = False

          if name == '':
               blank_name = True

          if not blank_name:
               if(bool(re.match('^[a-zA-Z0-9_]*$', name)) == True):
                    name_check = True
               
               room_check = ChatRoom.objects.filter(name = name)

               if name_check==True:
                    if not room_check:
                         key = str(shortuuid.uuid()[:10])
                         #datetime.now().strftime('%Y%m-%d%H-%M%S-') 
                         new_room = ChatRoom( name=name, mode=mode, key=key)
                         new_room.save()
                         new_room.connect_user(c_user)
                    else:
                         messages.info(request,"Already have a chat box on this name use number instead!")
               else:
                    messages.info(request,"Special character is not valid naming! Please use a-z or A-Z and 0-9 naming. ")
          else:
               messages.error(request,"Opps! You tried with a blank name! Please try with a propper  name!")

          c_user = request.user
          my_rooms = ChatRoom.objects.filter(users__username=c_user)

          return render(request, 'inbox.html', context={'my_rooms':my_rooms})

class Global(LoginRequiredMixin, View):
     def get(self,request,*args, **kwargs):

          c_user = request.user
          public_rooms = ChatRoom.objects.filter(mode=False).exclude(users__username=c_user)

          return render(request, 'global.html', context={'pu_rooms':public_rooms})

     def post(self, request, *args, **kwargs):
          c_user =request.user
          key = request.POST['key']
          try:
               key_room = ChatRoom.objects.get(key=key)
               if key_room:
                    key_room.connect_user(c_user)
                    return HttpResponseRedirect(reverse('chat:room',kwargs={'room_name': key_room.name }))
          except:
               messages.warning(request,"Wrong key!")
          return HttpResponseRedirect(reverse('chat:global'))
     
          
          
@login_required
def join_box(request,room_name):
     c_user =request.user
     box = ChatRoom.objects.get(name=room_name)

     box.connect_user(c_user)
     return HttpResponseRedirect(reverse('chat:room',kwargs={'room_name': room_name }))

@login_required
def leave_box(request,room_name):
     c_user =request.user
     box = ChatRoom.objects.get(name=room_name)

     success = box.disconnect_user(c_user)
     if success:
          messages.success(request,"Succesfully disconnected")
     return HttpResponseRedirect(reverse('chat:home'))