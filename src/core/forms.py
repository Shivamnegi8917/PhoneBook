from django import forms
from .models import PhoneBook

class ContactForm(forms.ModelForm):
    class Meta:
        model = PhoneBook
        fields = ['firstname','lastname','workplace','email','phone','age']
        