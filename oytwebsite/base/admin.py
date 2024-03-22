from django.contrib import admin

from base.models import Book, Faq, Movie

admin.site.register(Faq)
admin.site.register(Book)
admin.site.register(Movie)
