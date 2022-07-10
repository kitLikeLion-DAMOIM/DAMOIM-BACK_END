from django.db import router
from django.urls import path, include
from .views import PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('post',PostViewSet)

post_list = PostViewSet.as_view({
    'get':'list',
    'post':'create'
})

post_detail = PostViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy'
})

urlpatterns = [
    path('',post_list),
    path('<int:pk>/',post_detail),
]
