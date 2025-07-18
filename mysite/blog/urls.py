from django.urls import path
from .import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('blog/more1/', views.blog_more1, name='blog_more1'),
    path('blog/more2/', views.blog_more2, name='blog_more2'),
    path('blog/more3/', views.blog_more3, name='blog_more3'),
    path('blog/map/', views.map_view, name='map_view'),
]