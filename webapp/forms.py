from django import  forms
from webapp.models import modelform
class formmodel(forms.ModelForm):
    class Meta:
        model=modelform
        fields='__all__'
