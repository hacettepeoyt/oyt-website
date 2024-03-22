from django.contrib import admin

from user.models import Member, BoardMember

admin.site.register(Member)
admin.site.register(BoardMember)
