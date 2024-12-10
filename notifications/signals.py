# myapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from chat_messages.models import Message,
from .models import  Notification

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.recipient,
            message=f'You have a new message from {instance.sender.username}'
        )