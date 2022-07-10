from django.db import router
from django.urls import path, include
from .views import GroupViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('group',GroupViewSet)

group_list = GroupViewSet.as_view({
    'get' : 'list',
    'post' : 'create'
})

urlpatterns = [
    path('',group_list),
]