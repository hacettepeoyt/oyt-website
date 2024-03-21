from PIL import Image
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Project(models.Model):
    image = models.ImageField(upload_to='project/')
    title = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    status = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    repository_url = models.URLField()
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
