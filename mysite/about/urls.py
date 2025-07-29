from django.urls import path
from .import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('student/', views.std_info, name='std_info'),
    path('userCreate/', views.user_creation_form, name='user_creation_form'),
    path('userLogin/', views.user_login, name='user_login'),
]