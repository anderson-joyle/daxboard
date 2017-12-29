from django import forms

class SigninForm(forms.Form):
    resource = forms.URLField()
    tenant = forms.CharField()
    client_id = forms.CharField() 
    client_secret = forms.CharField()
    user_name = forms.EmailField()
