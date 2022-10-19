from django.contrib import admin
from django.urls import path

from Q_option import views

urlpatterns = [
    path('show/',views.showpage,name="show"),
    path('add/', views.addQuestion,name='add'),
]