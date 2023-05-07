from django import forms
from django.forms.widgets import DateInput

class SponsorForm(forms.Form):
    nama = forms.CharField(max_length=50)
    tgl_mulai = forms.DateField(widget=DateInput())
    tgl_selesai = forms.DateField(widget=DateInput())
