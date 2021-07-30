from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from .models import Client


class ExtendedAccountCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

        labels = {
            'username': _('Придумайте логин'),
            'email': _('Электронная почта'),
            'first_name': _('Имя'),
            'last_name': _('Фамилия'),
        }

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user


class AdditionalClientInfoForm(ModelForm):
    class Meta:
        model = Client
        fields = ('address', 'phone_number')
