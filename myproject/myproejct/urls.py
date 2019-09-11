"""myproejct URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('signin', views.signin, name='signin'),
    path('intro', views.intro, name='intro'),
    path('funding', views.funding, name='funding'),
    path('join', views.join, name='join'),
    path('test', views.test, name='test'),
    path('info', views.info, name='info'),
    path('list', views.list, name='list'),
    path('signup',views.signup,name='signup'),
    path('signout',views.signout,name='signout'),
]
