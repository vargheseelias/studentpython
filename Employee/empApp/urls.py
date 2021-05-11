from django.urls import path
from empApp import views

app_name = "empApp"
urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),
    path('register', views.EmployeeCreate.as_view(), name="register"),
    path('list', views.EmployeeList.as_view(), name="list"),
    path('details/<int:pk>', views.EmployeeDetails.as_view(), name="details"),
]
