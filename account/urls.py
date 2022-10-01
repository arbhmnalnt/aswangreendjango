from django.urls import path, include
from .views import *


app_name = "account"

urlpatterns = [
    path('register', register.as_view(), name='register'),
    path('login', login.as_view(), name='login')
]