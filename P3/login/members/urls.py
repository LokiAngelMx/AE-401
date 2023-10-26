from django.urls import path
from .views import register
from .views import home

urlpatterns = [
    path('register/', register, name='register'),
    path('', home, name='home'),
]
