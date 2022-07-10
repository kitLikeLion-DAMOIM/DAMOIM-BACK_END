from django.contrib import admin
from django.urls import path,include
from post import urls as post_urls
from account import urls as account_urls
from comment import urls as comment_urls
from group import urls as group_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('group.urls')),
    path('post/', include('post.urls')),
    path('account/',include('account.urls')),
    path ('comment',include('comment.urls')),
    ]
