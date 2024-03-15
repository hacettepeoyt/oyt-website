from django.contrib import admin

from .models import Book, Faq, Movie

admin.site.register(Faq)
admin.site.register(Book)
admin.site.register(Movie)
