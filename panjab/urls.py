from django.urls import path
from panjab.views import *
app_name='anything'
urlpatterns=[
    path('shikar/',shikar,name='shikar')
]