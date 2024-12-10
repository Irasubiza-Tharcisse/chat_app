from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Message(models.Model):
  sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
  recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  is_read = models.BooleanField(default=False)
  def __str__(self):
      return f'Message from {self.sender.username} to {self.recipient.username}'