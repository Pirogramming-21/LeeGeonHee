from django import forms
from .models import devtools

class devtoolsForm(forms.ModelForm):
    class Meta():
        model = devtools
        fields = ('__all__')