from django.db import models
from django.utils import timezone
# Create you
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='post-img')
