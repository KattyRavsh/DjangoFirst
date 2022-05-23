from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('items/', views.items_list, name="items-list"),
    path('item/<int:id>/', views.item, name="items-page"),
  
]
