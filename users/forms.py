from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput())
    password = forms.CharField(
        widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name',
                   'last_name',
                   'username',
                   'email',
                   'password1',
                   'password2'
                   ]
        
class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['image',
                   'first_name',
                   'last_name',
                   'username',
                   'email'
                   ]
        
    image = forms.FileField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
        
