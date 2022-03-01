from django.urls import path
from .views import Home, Room
app_name = 'chat'

urlpatterns = [
    path('', Home.as_view() , name='home'),
    path('<str:room_name>/', Room.as_view() , name='room'),
]
