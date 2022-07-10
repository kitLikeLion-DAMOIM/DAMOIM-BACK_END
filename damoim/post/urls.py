from django.db import router
from django.urls import path, include
from .views import PostViewSet,PostListViewSet,PostCreateViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('post',PostViewSet)

post_list = PostListViewSet.as_view({
    'get':'list',
})

post_detail = PostViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy'
})
post_create = PostCreateViewSet.as_view({
    'get':'list',
    'post':'create',
})

urlpatterns = [
    path('',post_list),
    path('detail/<int:pk>/',post_detail),
    path('create/<int:pk>/',post_create),
]
