from django import forms
from administration.models import ContactUs, Subscriber, Order


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name', 'style': 'width: 49%'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'style': 'width: 50%'}),
            'subject': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Subject', 'style': 'width: 240%'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 8}),
        }


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.TextInput(
                attrs={'class': 'searchTerm', 'placeholder': "Your Email", 'autocomplete': "off", 'width': '70%'})
        }
        labels = {
            "email": ""
        }


class ReserveForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email','delivery_date', 'delivery_time', 'phone', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name*', 'style': 'width: 49%'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name*', 'style': 'width: 49%'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email*', 'style': 'width: 49%'}),
            'delivery_date': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Delivery Date*', 'type':'date', 'style': 'width: 49%'} ),
            'delivery_time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Delivery Time*', 'type':'time', 'style': 'width: 49%'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email*', 'style': 'width: 49%'}),
            'phone': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Phone*', 'style': 'width: 49%'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write Item and Quantities', 'rows': 8}),
        }
