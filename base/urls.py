from django.contrib import admin
from django.urls import path
from django.views import View
from . import views


urlpatterns = [
    path('login/', views.loginRegister, name = "login"),
    path('logout/', views.logoutuser, name = "logout"),
    path('register/', views.registeruser, name = "register"),
    path('', views.home, name = "home"),
    path('room/<str:pk>/', views.room, name = "room"),
    path('create-room/', views.createroom, name = "createroom"),
    path('edit-room/<str:pk>/', views.updateroom, name = "editroom"),
    path('delete-room/<str:pk>/', views.deleteroom, name = "deleteroom"),
    path('delete-message/<str:pk>/', views.deletemessage, name = "deletemessage"),
    path('user-profile/<str:pk>/', views.userprofile, name = "userprofile"),
    path('edit-user/<str:pk>/', views.updateuser, name = "edituser"),
    path('topics/', views.topics, name = "topics"),
    path('activity/', views.activitypage, name = "activity"),
    path('lastmessage/<str:name>', views.lastMessage, name = "lastmessage"),
]