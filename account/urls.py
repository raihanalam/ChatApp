from django.urls import path
from . import views


app_name = 'account'

urlpatterns = [
     path('signup', views.sign_up, name='sign_up'),
     path('signin',views.sign_in, name='sign_in'),
     path('change_pro_pic/',views.change_pro_pic, name='change_pro_pic'),
     path('add_pro_pic/',views.add_pro_pic, name='add_pro_pic'),
     path('password/',views.change_password,name='change_password'),
     path('signout',views.sign_out,name='sign_out')
]