from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(
        label='İsim',
        max_length=32,
        widget=forms.TextInput(attrs={
            'class': 'form-control bg-white border-left-0 border-md',
            'placeholder': 'İsim'
        }),
        error_messages={
            'required': 'İsmini boş bırakamazsın!',
            'max_length': 'Eğer 32 karakterden uzunsa ismin, kısalt lütfen :)'
        }
    )
    last_name = forms.CharField(
        label='Soyisim',
        max_length=32,
        widget=forms.TextInput(attrs={
            'class': 'form-control bg-white border-left-0 border-md',
            'placeholder': 'Soyisim'
        }),
        error_messages={
            'required': 'Soyismini boş bırakamazsın!',
            'max_length': 'Eğer 32 karakterden uzunsa soyismin, kısalt lütfen :)'
        }
    )
    email = forms.EmailField(
        label='Eposta Adresi',
        max_length=320,
        widget=forms.EmailInput(attrs={
            'class': 'form-control bg-white border-left-0 border-md',
            'placeholder': 'Eposta Adresi'
        }),
        error_messages={
            'required': 'Eposta adresini boş bırakamazsın!',
            'max_length': '320 karakterden uzun eposta adresi mi olur ya?',
            'invalid': 'Geçersiz bir eposta adresi girdin!'
        }
    )
    message = forms.CharField(
        label='Mesajınız',
        widget=forms.Textarea(attrs={
            'class': 'form-control bg-white border-left-0 border-md',
            'placeholder': 'Mesajınız',
            'rows': 7
        }),
        error_messages={
            'required': 'Bir şeyler söyle de anlayalım ne istediğini =)',
        }
    )
    captcha = forms.IntegerField(
        label='Yandaki işlemin sonucunu giriniz',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'İşlemin sonucunu giriniz'
        }),
        error_messages={
            'required': 'Captcha boş bırakılmaz!',
        }
    )

    def clean(self):
        cleaned_data = super().clean()

        # Format first name and last name with single space separation, make them Title Case
        if cleaned_data.get('first_name'):
            cleaned_data['first_name'] = ' '.join(cleaned_data['first_name'].split()).title()

        if cleaned_data.get('last_name'):
            cleaned_data['last_name'] = ' '.join(cleaned_data['last_name'].split()).title()

        # Convert email to lowercase
        if cleaned_data.get('email'):
            cleaned_data['email'] = cleaned_data['email'].lower()

        return cleaned_data
