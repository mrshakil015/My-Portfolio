from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('home2/',home2,name='home2')
]