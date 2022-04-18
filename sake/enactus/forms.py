from django import forms

class RegisterForm(forms.Form):
    uname = forms.CharField()
    umail = forms.CharField()
    Pass = forms.CharField(widget = forms.PasswordInput())
    cpass = forms.CharField(widget = forms.PasswordInput())