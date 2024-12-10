from django.urls import path
from . import views
urlpatterns =[
  path('recieved_messages/', views.recieved_messages_view, name='recieved_messages'),
  path('chat/', views.chat_messages_view, name='chat_messages'),
]