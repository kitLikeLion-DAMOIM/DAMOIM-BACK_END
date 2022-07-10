from django.db import router
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()

# router.register('account',AccountViewSet)

# account_list = AccountViewSet.as_view({
    
# })

# account_detail = AccountViewSet.as_view({
    
# }) 

urlpatterns = [
    path('api-auth/',include('rest_framework.urls')),
    path('signup/',views.UserCreate.as_view()),
    path('login/',views.login)
]
