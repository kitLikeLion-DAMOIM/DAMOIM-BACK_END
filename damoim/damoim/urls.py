from django.contrib import admin
from django.urls import path,include
from post import urls
from account import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
    path('account/',include('account.urls')),
    ]
