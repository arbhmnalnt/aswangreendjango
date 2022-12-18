import json
from logging import exception
from sre_parse import CATEGORIES
from unicodedata import category
from django.shortcuts import HttpResponse, HttpResponseRedirect, redirect, render
from rest_framework.response import Response
from django.urls import is_valid_path, reverse
from django.views.generic.list import ListView
from rest_framework.views import APIView
# from symbol import pass_stmt
from DataEntry.models import *
from django.contrib.auth.decorators import login_required
from datetime import *
from django.contrib.auth.models import Group
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
@csrf_exempt
def login(request):
    message = ''
    if request.method == 'POST':
        email=request.POST['email']
        password = request.POST['password']
        user = login_user(email,password)
        if user is not None:
            auth_login(request, user)
            return redirect('/cAccounts/profile/')
            # message = f'Hello {user.username}! You have been logged in'
        else:
            message = 'خطأ بإسم المستخدم أو كلمة السر'
    else:
        message = ''
    ctx = {'msg':message}
    return render(request, './cAccounts/login.html', ctx)



# ============================================= FUNCTION PART =====================================================
def login_user(email, password):
    user_objects = Employee.objects.filter(email=email, password=password)
    if user_objects.count() == 1:
        user = user_objects[0]
    elif user_objects.count() == 0:
        user = None
        print(f"user with this email {email} is not found")
    else:
        print(f"proplem with users may be that user is not unique or not found => {email}")
    return user

def profile():
    pass