from django import forms
from portal.models import Application


class addApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        exclude = ['ip', 'state', 'service']