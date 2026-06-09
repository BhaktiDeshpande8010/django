from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('reg/', views.registration),
    path('saveform/', views.saveform),

    path('viewstudent/', views.viewstudent, name='viewstudent'),
    path('deletestudent/<int:id>', views.deletestudent),
    path('updatestudent/<int:id>', views.updatestudent),
    path('profileupdate/', views.profileupdate),

    path('login/', views.login, name='login'),
    path('logincheck/', views.logincheck, name='logincheck'),

    path('dashboard/', views.dashboard),
    path('logout/', views.logout),
]