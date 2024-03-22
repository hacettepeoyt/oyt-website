from PIL import Image
from django.db import models


class Event(models.Model):
    image = models.ImageField(upload_to='event/')
    title = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    location = models.CharField(max_length=128)
    date = models.DateTimeField()
    duration = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 1000 or img.width > 1000:
            output_size = (1000, 1000)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Course(models.Model):
    image = models.ImageField(upload_to='course/')
    title = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    pre_requisites = models.TextField(blank=True)
    location = models.CharField(max_length=128)
    date = models.DateTimeField()
    duration = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 1000 or img.width > 1000:
            output_size = (1000, 1000)
            img.thumbnail(output_size)
            img.save(self.image.path)
