from django.db import router
from django.urls import path, include
from .views import CommentViewSet
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('comment',CommentViewSet)

comment_list= CommentViewSet.as_view({'get':'list','post':'create'})

urlpatterns = [
    path('',comment_list),
]
