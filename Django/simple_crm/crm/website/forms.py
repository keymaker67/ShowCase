from django import forms

from .models import Record


class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = Record
        exclude = ('user', )

    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name'
                       ''}), label='')
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name'
                       ''}), label='')
    age = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Age'
    }), label='')
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Phone'
    }), label='')
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Address'
    }), label='')
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'City'
    }), label='')
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'State'
    }), label='')
    country = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Country'
    }), label='')
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Zipcode'
    }), label='')
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }), label='')
