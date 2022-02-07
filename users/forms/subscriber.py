from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class SubscriberSignupForm(forms.Form):
    username = forms.CharField(label=_('Username'), max_length=30)
    first_name = forms.CharField(label=_('First Name'), max_length=30)
    last_name = forms.CharField(label=_('Last Name'), max_length=30)
    email = forms.CharField(label=_('Email Address'), max_length=100)
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password1 = forms.CharField(label=_('Confirm Password'),
                                widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(SubscriberSignupForm, self).clean()
        password = cleaned_data.get("password")
        password1 = cleaned_data.get("password1")

        if password != password1:
            self.add_error('password', _('The passwords do not match'))
            self.add_error('password1', _('The passwords do not match'))
            raise forms.ValidationError(
                _("The passwords do not match")
            )
        if len(password) < 8:
            self.add_error('password',
                           _('Passwords must be at least 8 characters'))
            raise forms.ValidationError(
                _("Passwords must be at least 8 characters")
            )

    def clean_email(self):
        email = self.cleaned_data['email']
        existing = User.objects.filter(username=email).exists()
        if existing:
            raise forms.ValidationError(_("Email is no longer available."))
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        existing = User.objects.filter(username=username).exists()
        if existing:
            raise forms.ValidationError(_("Username is no longer available."))
        return username

