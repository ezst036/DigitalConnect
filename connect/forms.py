from django import forms
from . models import ContactConnect

class ConnectForm(forms.ModelForm):
    
    class Meta:
        model = ContactConnect
        fields = ['first_name', 'last_name', 'messagetype', 'title', 'body']
        labels = {
            'messagetype': 'Select message: ',
        }