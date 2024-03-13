from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, HTML, Div
from django import forms

from .models import Member


class EnrollForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self):
        super().__init__()
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Fieldset(
                '',
                input_with_icon('bi bi-person', 'first_name', 'İsim'),
                input_with_icon('bi bi-person', 'last_name', 'Soyisim'),
                input_with_icon('bi bi-123', 'student_id', 'Öğrenci Numası'),
                input_with_icon('bi bi-building', 'department', 'Bölüm'),
                input_with_icon('bi bi-list-ol', 'degree', 'Sınıf'),
                input_with_icon('bi bi-envelope', 'email', 'Mail Adresi'),
                input_with_icon('bi bi-telephone', 'mobile_number', 'Telefon Numarası'),
                input_with_icon('bi bi-chat-left-text', 'group_chat_platform', 'Size nereden ulaşalım?'),
                input_with_icon('bi bi-send', 'message', 'Söyleyemek istedikleriniz?'),
            ),
            Submit('submit', 'Üye Ol', css_id='signup-btn')
        )

    class Meta:
        model = Member
        fields = ['first_name',
                  'last_name',
                  'student_id',
                  'department',
                  'degree',
                  'email',
                  'mobile_number',
                  'group_chat_platform']


def input_with_icon(icon_class, field_name, placeholder):
    return Div(
        Div(
            HTML(
                f"""<span class="m-3">
                    <i class="{icon_class} fs-2" style="color: #ff4100;"></i>
                </span>"""
            ),
            css_class='input-group-prepend'
        ),
        field_name,
        css_class='input-group mb-3',
        placeholder=placeholder
    )
