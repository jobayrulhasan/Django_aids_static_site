from django.urls import path
from .import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('student/', views.std_info, name='std_info'),
]