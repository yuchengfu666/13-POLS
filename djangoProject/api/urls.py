from django.contrib import admin
from django.urls import path
from api.views import login

urlpatterns = [
    path('login/', login.LoginView.as_view()),
    path('sign/', login.SignView.as_view()),
]
