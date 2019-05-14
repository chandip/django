from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Tester(models.Model):
    title = models.CharField(max_length=255, blank = True)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=30, blank=True)

    date_posted = models.DateTimeField(default=timezone.now, blank = True)
    updated_date = models.DateTimeField(default=timezone.now, blank = True)
# Create your models here.

    def __str__(self):
        return self.title or str(self.slug)