from django.db import models
from django.utils import timezone
# Create your models here.
class user_profile(models.Model):
  created_at = models.DateTimeField(default=timezone.now)
  user_phone = models.CharField(max_length=100, blank=True, null=False)
  user_address = models.CharField(max_length=100, blank=True, null=False)
  password = models.CharField(max_length=100, blank=True, null=False)