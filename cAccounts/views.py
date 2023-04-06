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
from django.contrib.auth import logout as customLogout
# Create your views here.

def logout(request):
    customLogout(request)
    return redirect ('/cAccounts/login')

@csrf_exempt
def login(request):
    message = ''
    if request.method == 'POST':
        data2 = request.POST
        # print(data2)
        #data2 = json.loads(json.dumps(request.bo))
        
        username = data2.get('username')
        # print(f"username => {username}")
        password = data2.get('password')
        user = authenticate(username=username,password=password)
        # print(f"user => {user}")
        if user is not None:
            auth_login(request, user)
            return redirect('/cAccounts/profile')
            # message = f'Hello {user.username}! You have been logged in'
        else:
            message = 'خطأ بإسم المستخدم أو كلمة السر'
    else:
        message = ''
    ctx = {'msg':message}
    return render(request, './cAccounts/login.html', ctx)

# ============================================= FUNCTION PART =====================================================
# def login_user(email, password):
#     user_objects = Employee.objects.filter(email=email, password=password)
#     if user_objects.count() == 1:
#         user = user_objects[0]
#     elif user_objects.count() == 0:
#         user = None
#         print(f"user with this email {email} is not found")
#     else:
#         print(f"proplem with users may be that user is not unique or not found => {email}")
#     return user


def profile(request):
    user = request.user
    request.session.setdefault('group', False)
    print(f"user groups => {user.groups.all()}")
    if user.groups.filter(name="adminAll"):
        request.session['group'] = "adminAll"
        return redirect('/adminAll/')

    elif user.groups.filter(name="dataEntryAdmin"):
        request.session['group'] = "dataEntryAdmin"
        return redirect('/DataEntry/TmainPage')

    elif user.groups.filter(name="tahsealAdmin"):
        request.session['group'] = "tahsealAdmin"
        # print("admin here => ")
        return redirect('/DataEntry/TmainPage')
    
    elif user.groups.filter(name="ServiceManagerAdmin"):
        request.session['group'] = "ServiceManagerAdmin"
        # print("admin here => ")
        return redirect('/moreServicesManager/')
        
    else:
        request.session['group'] = "else"
        msg="user has no group"
        return redirect(f'/cAccounts/erorr_page?={msg}')
