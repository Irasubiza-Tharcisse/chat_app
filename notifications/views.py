from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your views here.

def recieved_notifications_view(request):
  notifications = request.user.notifications.all()
  context ={
    'notifications':notifications
  }
  return render(request,'notifications/recieved_notifications.html',context)