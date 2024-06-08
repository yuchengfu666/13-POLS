from django.shortcuts import render, HttpResponse, redirect
import requests
from app.models import UserInfo
from django.http import JsonResponse
import json
from app.utils.random_code import random_code
from django import forms
from django.contrib import auth


def index(request):
    return render(request, "index.html", {"request": request})


# Create your views here.
def user_list(request):
    return render(request, "user_list.html")


def tpl(request):
    name = "Nandemonaiya"
    roles = ["aa", "bb", "cc"]
    user_info = {"name": "Nandemonaiya", "roles": "CEO", "salary": 10000}

    return render(request, 'tpl.html', {"n1": name, "n2": roles, "n3": user_info})


def news(request):
    return render(request, 'news.html')


def info_list(request):
    #UserInfo.objects.create(name="Nandemonaiya", password="123", age=18)
    #UserInfo.objects.create(name="abc", password="321", age=23)
    data_list = UserInfo.objects.all()
    return render(request, 'info_list.html', {"data_list": data_list})


def info_add(request):
    if request.method == "GET":
        return render(request, 'info_add.html')
    user = request.POST.get('user')
    password = request.POST.get('pwd')
    age = request.POST.get('age')
    UserInfo.objects.create(name=user, password=password, age=age)
    return redirect('/info/list/')


def info_delete(request):
    uid = request.GET.get('id')
    UserInfo.objects.filter(id=uid).delete()
    return redirect('/info/list/')


def depart_list(request):
    """部门列表"""
    return render(request, 'depart_list.html')


def login(request):
    return render(request, 'login.html')


def sign(request):
    return render(request, 'sign.html')


# 获取随机验证码
def get_random_code(request):
    data, valid_code = random_code()
    request.session['valid_code'] = valid_code
    return HttpResponse(data)


def logout(request):
    auth.logout(request)
    return redirect('/index')
