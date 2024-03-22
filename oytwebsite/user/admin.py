import csv
from datetime import date

from django.contrib import admin
from django.http import HttpResponse

from user.models import Member, BoardMember


@admin.action(description="Download the selected members as CSV")
def download_csv(modeladmin, request, queryset):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': f'attachment; filename="members_{date.today()}.csv"'}
    )

    writer = csv.writer(response)
    fields = [field.name for field in Member._meta.get_fields()]

    # Exclude specific fields
    fields_to_exclude = ['id', 'updated_at', 'is_active']
    fields = [field for field in fields if field not in fields_to_exclude]

    writer.writerow(fields)

    for member in queryset:
        row = [getattr(member, field) for field in fields]
        writer.writerow(row)

    return response


class MemberAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'first_name', 'last_name', 'department', 'created_at']
    actions = [download_csv]


admin.site.register(Member, MemberAdmin)
admin.site.register(BoardMember)
