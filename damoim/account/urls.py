from django.db import router
from django.urls import path, include
from .views import AccountViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('account',AccountViewSet)

# account_list = AccountViewSet.as_view({
    
# })

# account_detail = AccountViewSet.as_view({
    
# }) 

urlpatterns = [
    path('',include(router.urls)),
    # path('blog/',blog_list),
    # path('blog/<int:pk>/',blog_detail),
]
