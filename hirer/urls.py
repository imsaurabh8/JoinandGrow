from django.contrib import admin
from django.urls import path
from . import views


app_name='hirer'

urlpatterns = [
    path("", views.search, name="search"),

    path("employees/",views.employees,name="employees"),


]