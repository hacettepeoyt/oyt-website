from django.forms import ModelForm

from .models import Member


class EnrollForm(ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'student_id', 'department', 'degree', 'email', 'mobile_number',
                  'group_chat_platform']
