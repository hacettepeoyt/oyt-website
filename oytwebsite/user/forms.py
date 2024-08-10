from django import forms

from user.models import Member


class EnrollForm(forms.ModelForm):
    message = forms.CharField(
        label='Mesajınız',
        widget=forms.Textarea(attrs={
            'class': 'form-control bg-white border-left-0 border-md',
            'placeholder': 'Mesajınız',
            'rows': 7
        }),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Update input widgets
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control bg-white border-left-0 border-md',
            'placeholder': 'İsim'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control bg-white border-left-0 border-md',
            'placeholder': 'Soyisim'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control bg-white border-left-0 border-md',
            'placeholder': 'Eposta Adresi'
        })
        self.fields['department'].widget.attrs.update({
            'class': 'form-control bg-white border-left-0 border-md',
            'placeholder': 'Bölümünüz'
        })
        self.fields['degree'].widget.attrs.update({
            'class': 'form-select',
        })
        self.fields['mobile_number'].widget.attrs.update({
            'class': 'form-control bg-white border-md border-left-0',
            'placeholder': 'Telefon Numarası'
        })
        self.fields['student_id'].widget.attrs.update({
            'class': 'form-control bg-white border-left-0 border-md',
            'placeholder': 'Öğrenci Numarası'
        })
        self.fields['group_chat_platform'].widget.attrs.update({
            'class': 'form-select',
        })

        # Set default values for select type of inputs
        self.fields['degree'].initial = 'Hazırlık'
        self.fields['group_chat_platform'].initial = 'Signal'

    def clean(self):
        cleaned_data = super().clean()

        # Format with single space separation, make them Title Case
        if cleaned_data.get('first_name'):
            cleaned_data['first_name'] = ' '.join(cleaned_data['first_name'].split()).title()

        if cleaned_data.get('last_name'):
            cleaned_data['last_name'] = ' '.join(cleaned_data['last_name'].split()).title()

        if cleaned_data.get('department'):
            cleaned_data['department'] = ' '.join(cleaned_data['department'].split()).title()

        # There are two types of id. One for regular students, and for international students.
        # "2210356075" is an example for regular students.
        # "Y2210356075" is an example for international students.
        if cleaned_data.get('student_id'):
            cleaned_data['student_id'] = ''.join(cleaned_data['student_id'].split()).upper()

        # This piece of code is written by the assumption of phone codes belongs to Türkiye.
        # If the user writes with any other code, like +48, it's okay though. It's just important
        # when there is a need to complete prefix.
        if cleaned_data.get('mobile_number'):
            initial_mobile_number = ''.join(cleaned_data['mobile_number'].split())

            if initial_mobile_number[:2] == '90':
                cleaned_data['mobile_number'] = '+' + initial_mobile_number
            elif initial_mobile_number[0] == '0':
                cleaned_data['mobile_number'] = '+9' + initial_mobile_number
            elif initial_mobile_number[0] != '+':
                cleaned_data['mobile_number'] = '+90' + initial_mobile_number

        if cleaned_data.get('email'):
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
        error_messages = {
            'first_name': {
                'required': 'İsmini boş bırakamazsın!',
                'max_length': 'Eğer 32 karakterden uzunsa ismin, kısalt lütfen :)'
            },
            'last_name': {
                'required': 'Soyismini boş bırakamazsın!',
                'max_length': 'Eğer 32 karakterden uzunsa soyismin, kısalt lütfen :)'
            },
            'department': {
                'required': 'Departmanını boş bırakamazsın!',
                'max_length': 'Departman ismi 64 karakterden uzun olamaz!'
            },
            'degree': {
                'required': 'Sınıfını seçmek zorundasın!',
                'invalid': 'Lütfen listeden bir sınıf seçtiğinden emin ol!',
            },
            'email': {
                'required': 'Eposta adresini boş bırakamazsın!',
                'max_length': '320 karakterden uzun eposta adresi mi olur ya?',
                'invalid': 'Geçersiz bir eposta adresi girdin!',
            },
            'mobile_number': {
                'required': 'Telefon numarasını boş bırakamazsın!',
                'invalid': 'Geçersiz bir telefon numarası girdin!',
                'max_length': '15 karakterden daha uzun bir telefon numarası nasıl yazmış olabilirsin? Bkz: E.164'
            },
            'group_chat_platform': {
                'required': 'Sohbet kanalı seçmen gerekiyor!',
                'invalid': 'Lütfen geçerli bir sohbet kanalı seçtiğinden emin ol!'
            }
        }
