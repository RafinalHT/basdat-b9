from django import forms
from django.forms.widgets import DateInput

class AtletPelatihForm(forms.Form):
    id_atlet = forms.UUIDField()
