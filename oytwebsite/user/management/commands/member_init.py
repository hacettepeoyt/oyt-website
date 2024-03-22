# This script lets you save existing members from a csv file into your database.
# I'm writing because our system has been written from scratch and our old database
# used to be MongoDB. We need to move the old data back.
#
# Make sure that your csv file matches with the column names.


import csv

from django.core.management.base import BaseCommand

from user.models import Member


class Command(BaseCommand):
    help = 'Saves new members to database from a given csv file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                first_name = ' '.join(row['First Name'].strip().split()).title()
                last_name = ' '.join(row['Last Name'].strip().split()).title()
                department = ' '.join(row['Department'].strip().split()).title()
                student_id = ''.join(row['Student ID'].strip().split()).upper()
                degree = row['Degree'].strip()
                email = row['Email'].strip().lower()
                group_chat_platform = row['Group Chat']
                mobile_number = ''.join(row['Mobile Number'].strip().split())

                if mobile_number[:2] == '90':
                    mobile_number = '+' + mobile_number
                elif mobile_number[0] == '0':
                    mobile_number = '+9' + mobile_number
                elif mobile_number[0] != '+':
                    mobile_number = '+90' + mobile_number

                # Check if member already exists in the database
                existing_member = Member.objects.filter(student_id=student_id)
                if existing_member.exists():
                    self.stdout.write(
                        self.style.WARNING(f'{first_name} {last_name} already exists in the database. Skipping...')
                    )
                    continue

                member = Member(
                    first_name=first_name,
                    last_name=last_name,
                    department=department,
                    student_id=student_id,
                    degree=degree,
                    email=email,
                    mobile_number=mobile_number,
                    group_chat_platform=group_chat_platform
                )
                member.save()
                self.stdout.write(
                    self.style.SUCCESS(f'Saved {member.first_name} {member.last_name}')
                )
