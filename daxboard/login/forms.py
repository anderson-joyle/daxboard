from django import forms

class LoginForm(forms.Form):
    dynamics_fo_url = forms.URLField(max_length=256, label='D365 FO URL', required=False, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'D365 URL address'}))
    tenant = forms.CharField(label='Tenant', required=False, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Azure AD tenant'}))
    client_id = forms.CharField(label='Client id', required=False, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Azure AD client id'}))
    client_secret = forms.CharField(label='Client secret', required=False, widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Azure AD client secret'}))
    # email = forms.EmailField(label='Email account', required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email account'}))
    # password = forms.CharField(label='Password', required=False, widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Password'}))