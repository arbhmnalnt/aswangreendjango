from django.urls import path, include
from .views import *


app_name = "account"

urlpatterns = [
    path('activate', activate.as_view(), name='activate'),
    path('request_service', request_service.as_view(), name='request_service'),
    path('contact_us', contact_us.as_view(), name='contact_us'),
    # path('contact_us/suggest', contact_us.as_view(), name='contact_us'),
    # path('contact_us/complaint', contact_us.as_view(), name='contact_us'),
    path('offers', offers.as_view(), name='offer' ),
    #//
    path('profile/img', profileImage.as_view(), name='profile_img'),
    path('profile/edit', profile_edit.as_view(), name='profile_edit'),
    path('profile/view', profile_view.as_view(), name='profile_view'),
    path('registerFirstStep', registerFirstStep.as_view(), name='registerFirstStep'),
    path('registerFinal', registerFinal.as_view(), name='registerFinal'),
    path('login', login.as_view(), name='login')
]