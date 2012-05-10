from django import forms

__author__ = 'thacdu'

class ForgotPasswordForm(forms.Form):
    username=forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder":"Username"}), label="Username")
    email=forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder":"Email"}), label="Email")
