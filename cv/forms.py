from django import forms
from django.utils.html import escape
from django.utils.safestring import mark_safe
import html


from .models import Application


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = '__all__'
        exclude = ['first_email', 'second_email']

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'snippet':
                self.fields.get(field).widget.attrs.update({'class': 'myfield'})
        if (instance := kwargs.get('instance')) is not None:
            super(ApplicationForm, self).__init__(initial={'snippet': html.unescape(instance.snippet)}, *args, **kwargs)

    def clean_snippet(self):
        return escape(self.cleaned_data.get('snippet'))
