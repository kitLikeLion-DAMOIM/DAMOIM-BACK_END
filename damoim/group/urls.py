from django.db import router
from django.urls import path, include
from .views import GroupViewSet,GroupListViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('group',GroupViewSet)

group_list = GroupListViewSet.as_view({
    'get' : 'list',
})
group_detail = GroupViewSet.as_view({
    'get' : 'list',
})

urlpatterns = [
    path('',group_list),
    path('<int:pk>/',group_detail)
]