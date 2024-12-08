from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='uploads/')
    file_size = models.IntegerField(blank=True, null=True)  # Optional

    def __str__(self):
        return self.file_name

class DataItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

