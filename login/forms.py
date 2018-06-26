import re
from django import forms
from django.contrib.auth.models import User
from login.models import AuthUser
from django.utils.translation import ugettext_lazy as _
 
class RegistrationForm(forms.Form):
 
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=254)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))
    firstname = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("First Name"))
    lastname = forms.CharField(widget=forms.TextInput(attrs=dict(required=False, max_length=30)), label=_("Last Name"))
    affiliation = forms.CharField(widget=forms.TextInput(attrs=dict(required=False, max_length=254)), label=_("Affiliation"))
    experience = forms.CharField(widget=forms.TextInput(attrs=dict(required=False, max_length=512)), label=_("Experience"))
    interests = forms.CharField(widget=forms.TextInput(attrs=dict(required=False, max_length=512)), label=_("Interests"))
 
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))
 
    def clean(self):
        print(self.cleaned_data)
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data