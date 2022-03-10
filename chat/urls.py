from django.urls import path
from . import views
app_name = 'chat'

urlpatterns = [
    path('', views.Home.as_view() , name='home'),
    path('profile/', views.Profile.as_view() , name='profile'),
    path('inbox/', views.Inbox.as_view() , name='inbox'),
    path('global/',views.Global.as_view(), name='global'),
    path('box/<str:room_name>/', views.Room.as_view() , name='room'),
    path('join-box/<str:room_name>/',views.join_box, name="join_box"),
    path('leave-box/<str:room_name>/',views.leave_box, name="leave_box"),
]