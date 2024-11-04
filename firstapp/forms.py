from cProfile import label

from django import forms
from .models import ChaiVriety

class ChaiVrietyForm(forms.Form):
    ChaiVriety = forms.ModelChoiceField(queryset=ChaiVriety.objects.all(), label = "Select your chai variety: ")