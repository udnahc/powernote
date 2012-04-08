from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    email = forms.EmailField()

