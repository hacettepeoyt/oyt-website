from django.db import models


class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question


class Book(models.Model):
    cover = models.ImageField(upload_to='book/')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.IntegerField()
    description = models.TextField()
    resource_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title + " by " + self.author


class Movie(models.Model):
    cover = models.ImageField(upload_to='movie/')
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    year = models.IntegerField()
    genre = models.CharField(max_length=255)
    description = models.TextField()
    resource_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title + " by " + self.director
