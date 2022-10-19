from django.contrib import admin
from django.urls import path

from signin import views

urlpatterns = [
    path('',views.home,name="home"),
    path('signin/',views.newreg,name="signin"),
    path('login/',views.userlogin,name="login"),
    path('logout/',views.userlogout,name="logout"),

]