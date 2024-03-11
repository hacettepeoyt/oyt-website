from django import forms

from .models import Member


class EnrollForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'student_id', 'department', 'degree', 'email', 'mobile_number',
                  'group_chat_platform']
