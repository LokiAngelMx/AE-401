from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('change-password/', views.change_password_view, name='change_password'),
    path('', views.home, name='home'),
]