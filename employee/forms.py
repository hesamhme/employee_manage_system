from django import forms
from .models import Penalty

class PenaltyForm(forms.ModelForm):
    class Meta:
        model = Penalty
        fields = ('fee', ) 
