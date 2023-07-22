from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'), #+cf
    path('success/', views.success, name='blog-success') #+cf
]