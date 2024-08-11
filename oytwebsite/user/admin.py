import csv
from datetime import date

from django.contrib import admin
from django.http import HttpResponse

from user.models import Member, BoardMember


@admin.action(description='Download the selected members as CSV')
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


@admin.action(description='Download the selected members as VCF')
def download_vcf(modeladmin, request, queryset):
    response = HttpResponse(
        content_type='text/x-vcard',
        headers={'Content-Disposition': f'attachment; filename="members_{date.today()}.vcf"'}
    )

    vcf_lines = []
    current_year = date.today().year % 100

    for member in queryset:
        vcf_lines.append('BEGIN:VCARD')
        vcf_lines.append('VERSION:3.0')
        vcf_lines.append(f'FN:OYT{current_year}{member.group_chat_platform[0]} {member.first_name} {member.last_name}')
        vcf_lines.append(f'ORG:{member.department}')
        vcf_lines.append(f'TEL;TYPE=cell:{member.mobile_number}')
        vcf_lines.append(f'EMAIL:{member.email}')
        vcf_lines.append(f'NOTE:{member.student_id} - {member.degree}')
        vcf_lines.append('END:VCARD')

    response.content = "\n".join(vcf_lines)
    return response


class MemberAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'first_name', 'last_name', 'department', 'created_at']
    actions = [download_csv, download_vcf]


admin.site.register(Member, MemberAdmin)
admin.site.register(BoardMember)
