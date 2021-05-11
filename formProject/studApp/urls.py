from django.urls import path
from studApp import views

urlpatterns = [
    path('',views.getHome,name='home'),
    path('register',views.registration,name='register'),
]