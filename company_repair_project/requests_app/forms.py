from django.forms import ModelForm

from requests_app.models import Request


class NewRequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ('type', 'title', 'description')

