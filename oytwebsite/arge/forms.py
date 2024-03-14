from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, HTML, Field, Submit, Fieldset, Layout
from django import forms


class IdeaForm(forms.Form):
    first_name = forms.CharField(max_length=32, required=True)
    last_name = forms.CharField(max_length=32, required=True)
    email = forms.EmailField(required=True)
    project_title = forms.CharField(max_length=64, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = get_idea_form_layout()
        self.helper.form_show_labels = False


def get_idea_form_layout():
    return Layout(
        Fieldset(
            '',
            get_field_with_icon(icon_class='bi bi-person',
                                field_name='first_name',
                                placeholder='İsim'),
            get_field_with_icon(icon_class='bi bi-person',
                                field_name='last_name',
                                placeholder='Soyisim'),
            get_field_with_icon(icon_class='bi bi-envelope',
                                field_name='email',
                                placeholder='Mail Adresi'),
            get_field_with_icon(icon_class='bi bi-pencil',
                                field_name='project_title',
                                placeholder='Proje Adı'),
            get_field_with_icon(icon_class='bi bi-send',
                                field_name='message',
                                placeholder='Proje ilgili açıklamarı buraya yazabilirsiniz!'),
        ),
        Div(
            Div(
                css_class='col-sm-2 col-form-label text-end'
            ),
            Submit('submit', 'Gönder', css_id='signup-btn', css_class='col-sm-2 ms-3'),
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
