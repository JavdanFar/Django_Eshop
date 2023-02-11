from django import forms
from django.core import validators


class CreateContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'لطفا نام و نام خانوادگی خود را وارد کنید', 'class': 'form-control'}),
        label='نام و نام خانوادگی',
        validators=[validators.MaxLengthValidator(150, 'تعداد کاراکتر ها نمیتوانند بیشتر از 150 عدد باشند!')]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد کنید', 'class': 'form-control'}),
        label='ایمیل',
        validators=[validators.MaxLengthValidator(100, 'تعداد کاراکتر ها نمیتوانند بیشتر از 100 عدد باشند!')]
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا عنوان را وارد کنید', 'class': 'form-control'}),
        label='عنوان',
        validators=[validators.MaxLengthValidator(50, 'تعداد کاراکتر ها نمیتوانند بیشتر از 50 عدد باشند!')]
    )
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'لطفا پیام خود را وارد کنید', 'class': 'form-control', 'rows': '8'}),
        label='پیام'
    )
