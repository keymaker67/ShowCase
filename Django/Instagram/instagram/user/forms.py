from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

from .models import UserProfileModel

User = get_user_model()


# Create a form for accessing user profile data
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = ('public', 'profile_picture', 'bio', 'location')

    # user = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={
    #     'class': 'form-control', 'placeholder': 'Username'}), label='')
    # public = forms.BooleanField(required=True, widget=forms.widgets.NullBooleanSelect(attrs={
    #     'class': 'form-control', 'placeholder': 'Public', 'default': 'No'}), label='')
    # profile_picture = forms.ImageField(required=False, widget=forms.widgets.TextInput(attrs={
    #     'class': 'form-control', 'placeholder': 'Profile picture'}), label='')
    # bio = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={
    #     'class': 'form-control', 'placeholder': 'Biography'}), label='')
    # location = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={
    #     'class': 'form-control', 'placeholder': 'First Name'}), label='')


class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
