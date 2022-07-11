from django.db import router
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('new',views.comment_create)
]
