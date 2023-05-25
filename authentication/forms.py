from django import forms
from django.contrib.auth.forms import UserCreationForm


class LoginForm(UserCreationForm):
    nama = forms.CharField( widget=forms.TextInput( attrs={'id': 'nama', 'placeholder': 'Nama'}) )
    email = forms.CharField(widget=forms.TextInput( attrs={'id': 'email', 'placeholder': 'Email'}))


class RegisterAtletForm(UserCreationForm):
    nama = forms.CharField(widget=forms.TextInput(attrs={'id': 'register_nama', 'placeholder': 'Nama'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'id': 'register_email', 'placeholder': 'Email'}))
    negara = forms.CharField(widget=forms.TextInput(attrs={'id': 'register_negara', 'placeholder': 'Negara'}))
    tanggal_lahir = forms.DateField(label='register_tanggal_lahir', widget=forms.DateInput(attrs={'type': 'date'}))
    play = forms.CharField(widget=forms.RadioSelect(
        choices=[('1', 'Left'),
                ('2', 'Right')]))
    tinggi_badan = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'register_tinggi', 'placeholder': 'Tinggi badam'}))
    jenis_kelamin = forms.CharField(widget=forms.RadioSelect(
        choices=[('1', 'Laki-laki'),
                ('2', 'Perempuan')]))


class RegisterPelatihForm(UserCreationForm):
    nama = forms.CharField(widget=forms.TextInput(attrs={'id': 'register_nama_pelatih', 'placeholder': 'Nama'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'id': 'register_email_pelatih', 'placeholder': 'Email'}))
    negara = forms.CharField(widget=forms.TextInput(attrs={'id': 'register_negara_pelatih', 'placeholder': 'Negara'}))
    kategori = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        choices=[('tunggal putra', 'tunggal putra'),
                ('tunggal putri', 'tunggal putri'),
                ('ganda putra', 'ganda putra'),
                ('ganda putri', 'ganda putri'),
                ('ganda campuran', 'ganda campuran')])
    tanggal_mulai = forms.DateField(widget=forms.DateInput(attrs={'type': 'datetime-local'}))


class RegisterUmpireForm(UserCreationForm):
    nama = forms.CharField(widget=forms.TextInput(attrs={'id': 'register_nama_umpire', 'placeholder': 'Nama'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'id': 'register_email_umpire', 'placeholder': 'Email'}))
    negara = forms.CharField(widget=forms.TextInput(attrs={'id': 'register-_negara_umpire', 'placeholder': 'Negara'})
    )