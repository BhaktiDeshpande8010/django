from django.contrib import admin
from django.urls import path,include

from .import views

urlpatterns = [
    
    path('',views.home),
    path('about',views.about),
    path('reg/',views.registration),
    path('saveform/', views.saveform),
    path('viewstudent/', views.viewstudent, name='viewstudent'),

    # path('deletestudent',views.deletestudent),
    path('deletestudent/<int:id>',views.deletestudent),
    path('updatestudent/<int:id>',views.updatestudent),
    path('profileupdate/',views.profileupdate)
    
]