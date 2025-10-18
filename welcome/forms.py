from django import forms
from .models import OrdUdf

class OrdUdfForm(forms.ModelForm):
    class Meta:
        model = OrdUdf
        fields = '__all__' 
        # exclude = ['id', 'orderno']
