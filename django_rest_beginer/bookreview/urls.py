from django.contrib import admin
from django.urls import path,include
from .views import AuthorView,AuthorInstanceView

urlpatterns = [
    path('author/', AuthorView.as_view()),
    path('authors/<int:pk>', AuthorInstanceView.as_view(), name='author-instance')
]