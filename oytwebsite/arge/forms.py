from django import forms


class IdeaForm(forms.Form):
    first_name = forms.CharField(max_length=32, required=True)
    last_name = forms.CharField(max_length=32, required=True)
    email = forms.EmailField(required=True)
    project_title = forms.CharField(max_length=64, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
