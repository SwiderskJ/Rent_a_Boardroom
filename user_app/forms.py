from django import forms


class UserCreateForm(forms.Form):
    login = forms.CharField(label='Login')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    first_name = forms.CharField(label='First_name')
    last_name = forms.CharField(label='Last_name')
    email = forms.EmailField(label='Email')
    host = forms.BooleanField(label='Holder', required=False)


class LoginForm(forms.Form):
    username = forms.CharField(label='Login')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)