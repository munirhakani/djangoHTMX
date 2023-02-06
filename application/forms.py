from django import forms
from .models import Person as Object


class ObjectForm(forms.ModelForm):

    class Meta:
        model = Object
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ObjectForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'onfocusin': '$(this).select();'})