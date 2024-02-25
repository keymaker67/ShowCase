from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


UserModel = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = UserModel
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]