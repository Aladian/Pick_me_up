from django.contrib.auth.models import User
from django import forms
from .models import SignUp, Song, Album


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['location','station','time','is_full']

    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       super(SongForm, self).__init__(*args, **kwargs)
       self.fields['location'].queryset = Album.objects.filter(driver=user)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password']

class ContactForm(forms.Form):

    message = forms.CharField(widget=forms.Textarea)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base,provider = email.split("@")
        domain, extension = provider.split(".")
        # if not ".edu" in email:
        #     raise forms.ValidationError("Please use a valid .EDU email address")
        return email

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name','email']
        # exclude = ['full_name']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base,provider = email.split("@")

        domain, extension = provider.split(".")
        if not ".edu" in email:
            raise forms.ValidationError("Please use a valid .EDU email address")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        return full_name