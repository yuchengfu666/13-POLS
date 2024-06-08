"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from app import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('index/', views.index),
    path('admin/', admin.site.urls),
    path('user/list/', views.user_list),
    path('tpl/', views.tpl),
    path('news/', views.news),
    path('login/', views.login),
    path('info/list/', views.info_list),
    path('info/add/', views.info_add),
    path('info/delete/', views.info_delete),
    path('depart/list/', views.depart_list),
    path('sign/', views.sign),
    path('login/random_code/', views.get_random_code),
    path('logout/', views.logout),


    re_path(r'api/', include('api.urls')),  # 路由分发
]
