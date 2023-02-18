from django import forms
from administration.models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name', 'style': 'width: 49%'}),
            'email':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'style':'width: 50%'}),
            'subject':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject', 'style':'width: 240%'}),
            'message':forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows':8}),
        }
