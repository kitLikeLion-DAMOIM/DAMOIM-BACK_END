from django.db import router
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from comment import urls

# post_list = PostListViewSet.as_view({
#     'get':'list',
# })

# post_detail = PostViewSet.as_view({
#     'get':'retrieve',
#     'put':'update',
#     'delete':'destroy'
# })
# post_create = PostCreateViewSet.as_view({
#     'get':'list',
#     'post':'create',
# })

urlpatterns = [
    path('',views.post_list),
    path('detail/<int:pk>/',views.post_detail),
    path('detail/<int:pk>/comment/',include('comment.urls')),
    path('new',views.post_create)
]
