
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('ideaHub.urls')),
    path('',include('chat_messages.urls')),
    path('',include('notifications.urls')),
    path('',include('friends.urls')),
]
