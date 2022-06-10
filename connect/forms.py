from django import forms
from . models import ContactConnect

class ConnectForm(forms.ModelForm):
    
    class Meta:
        model = ContactConnect
        fields = ['title', 'body']