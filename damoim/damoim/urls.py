from django.contrib import admin
from django.urls import path,include
from post import urls
from account import urls 
from comment import urls 
from group import urls 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('group.urls')),
    path('account/',include('account.urls')),
    path('comment/',include('comment.urls'))
    ]
