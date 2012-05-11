from django import forms

__author__ = 'thacdu'

class ForgotPasswordForm(forms.Form):
    username=forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder":"Username"}), label="Username")
    email=forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder":"Email"}), label="Email")

class RegistrationForm(forms.Form):
    username=forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder":"Username", "id": "username"}), min_length=5, label="")
    email=forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder":"Email", "id":"email"}), label="")
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder":"Password", "id":"password"}), min_length=6, label="")
    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password", "id":"confirm_password"}), min_length=6, label="")