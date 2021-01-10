from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput
from home.models import UserProfile
from django.contrib.auth.forms import PasswordChangeForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label='Kullanıcı Adı',
        max_length=20
    )

    email = forms.EmailField(
        label='Email',
        max_length=40
    )

    first_name = forms.CharField(
        label='İsim',
        max_length=20
    )

    last_name = forms.CharField(
        label='Soyisim',
        max_length=20
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        )


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name','last_name')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone','address','city')

class PasswordChangingForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')