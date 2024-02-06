from django import forms
from .models import *

class registrationForm(forms.ModelForm):
    class Meta:
        model=registration
        fields='__all__'