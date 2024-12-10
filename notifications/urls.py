from django.urls import path
from . import views
urlpatterns =[
  path('recieved_notifications/',views.recieved_notifications_view,name='recieved_notifications'),
]