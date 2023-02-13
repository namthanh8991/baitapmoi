from django.contrib import admin
from django.urls import path,include
from .views import StudentView
urlpatterns = [
    path('a/', StudentView.as_view()),

]