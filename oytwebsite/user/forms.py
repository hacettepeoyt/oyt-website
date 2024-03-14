from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, HTML, Div, Field
from django import forms

from .models import Member


class EnrollForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = get_enroll_form_layout()
        self.helper.form_show_labels = False
        self.fields['degree'].initial = 'Hazırlık'
        self.fields['group_chat_platform'].initial = 'Signal'

    def clean(self):
        cleaned_data = super().clean()

        # Format with single space separation, make them Title Case
        cleaned_data['first_name'] = ' '.join(cleaned_data['first_name'].split()).title()
        cleaned_data['last_name'] = ' '.join(cleaned_data['last_name'].split()).title()
        cleaned_data['department'] = ' '.join(cleaned_data['department'].split()).title()

        # There are two types of id. One for regular students, and for international students.
        # "2210356075" is an example for regular students.
        # "Y2210356075" is an example for international students.
        cleaned_data['student_id'] = ''.join(cleaned_data['student_id'].split()).upper()

        # This piece of code is written by the assumption of phone codes belongs to Türkiye.
        # If the user writes with any other code, like +48, it's okay though. It's just important
        # when there is a need to complete prefix.
        initial_mobile_number = ''.join(cleaned_data['mobile_number'].split())

        if initial_mobile_number[:2] == '90':
            cleaned_data['mobile_number'] = '+' + initial_mobile_number
        elif initial_mobile_number[0] == '0':
            cleaned_data['mobile_number'] = '+9' + initial_mobile_number
        elif initial_mobile_number[0] != '+':
            cleaned_data['mobile_number'] = '+90' + initial_mobile_number

        cleaned_data['email'] = cleaned_data['email'].lower()
        return cleaned_data

    class Meta:
        model = Member
        fields = [
            'first_name',
            'last_name',
            'student_id',
            'department',
            'degree',
            'email',
            'mobile_number',
            'group_chat_platform'
        ]


def get_enroll_form_layout():
    return Layout(
        Fieldset(
            '',
            get_field_with_icon(icon_class='bi bi-person',
                                field_name='first_name',
                                placeholder='İsim'),
            get_field_with_icon(icon_class='bi bi-person',
                                field_name='last_name',
                                placeholder='Soyisim'),
            get_field_with_icon(icon_class='bi bi-123',
                                field_name='student_id',
                                placeholder='Öğrenci Numarası'),
            get_field_with_icon(icon_class='bi bi-building',
                                field_name='department',
                                placeholder='Bölüm'),
            get_field_with_icon(icon_class='bi bi-list-ol',
                                field_name='degree'),
            get_field_with_icon(icon_class='bi bi-envelope',
                                field_name='email',
                                placeholder='Mail Adresi'),
            get_field_with_icon(icon_class='bi bi-telephone',
                                field_name='mobile_number',
                                placeholder='Telefon Numarası'),
            get_field_with_icon(icon_class='bi bi-chat-left-text',
                                field_name='group_chat_platform'),
            get_field_with_icon(icon_class='bi bi-send',
                                field_name='message',
                                placeholder='Söylemek istedikleriniz?'),
        ),
        Div(
            Div(
                css_class='col-sm-2 col-form-label text-end'
            ),
            Submit('submit', 'Üye Ol', css_id='signup-btn', css_class='col-sm-2'),
            css_class='form-group row d-flex align-items-center',
        )
    )


def get_field_with_icon(icon_class, field_name, placeholder=None):
    return Div(
        Div(
            HTML(
                f"""
                    <i class="{icon_class} fs-2" style="color: #ff4100;"></i>
                """
            ),
            css_class='col-sm-2 col-form-label'
        ),
        Field(field_name, wrapper_class='pt-3 col-sm-10', placeholder=placeholder),
        css_class='form-group row d-flex align-items-center',
    )
