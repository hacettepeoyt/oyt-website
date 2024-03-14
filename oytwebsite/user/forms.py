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
                                placeholder='Söyleyemek istedikleriniz?'),
        ),
        Div(
            Div(
                css_class='col-sm-2 col-form-label text-end'
            ),
            Submit('submit', 'Üye Ol', css_id='signup-btn', css_class='col-sm-2 ms-3'),
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
            css_class='col-sm-2 col-form-label text-end'
        ),
        Field(field_name, wrapper_class='pt-3 col-sm-10', placeholder=placeholder),
        css_class='form-group row d-flex align-items-center',
    )
