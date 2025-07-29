from django.urls import path
from .import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('student/', views.std_info, name='std_info'),
    
    # authentication paths
    path('userCreate/', views.user_creation_form, name='user_creation_form'),
    path('userLogin/', views.user_login, name='user_login'),
    path('login_success/', views.successPage, name='successPage'),
    path('userlogout/', views.user_logout, name='user_logout'),
    path('changepassword/', views.change_password, name='change_password'),
    path('changepasswordsuccess/', views.passwordChangeSuccess, name='change_password_success'),
]