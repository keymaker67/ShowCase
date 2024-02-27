from django import forms

from .models import UserProfile


# Create a form for accessing user profile data
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user', ]

    user = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name'
                       ''}), label='')
    id_user = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name'
                       ''}), label='')
    public = forms.BooleanField(required=True, widget=forms.widgets.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name'
                       ''}), label='')
    profile_picture = forms.ImageField(required=False, widget=forms.widgets.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name'
                       ''}), label='')
    bio = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name'
                       ''}), label='')
    location = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name'
                       ''}), label='')
