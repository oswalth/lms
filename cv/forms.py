from django import forms
from django.utils.html import escape

from .models import Application


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = '__all__'
        exclude = ['first_email', 'second_email']

    def clean_snippet(self):
        return escape(self.cleaned_data.get('snippet'))
