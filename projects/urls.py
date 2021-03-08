from django.contrib import admin
from django.urls import include, path
from projects import views

urlpatterns = [
    path('', views.project_list),
]
