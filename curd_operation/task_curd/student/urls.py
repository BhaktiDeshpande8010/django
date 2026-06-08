from django.contrib import admin
from django.urls import path,include

from .import views

urlpatterns = [
    
    path('',views.home),
    path('about',views.about),
    path('reg/',views.registration),
    path('saveform/', views.saveform),
    
]