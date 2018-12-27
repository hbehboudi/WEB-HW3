from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Tweet(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=240)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date_time = models.DateTimeField(default=timezone.now)
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_date_time', "title"]
