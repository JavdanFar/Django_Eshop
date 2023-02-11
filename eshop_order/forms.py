from django import forms
from .models import UserAddress


class UserNewOrderForm(forms.Form):
    product_id = forms.IntegerField(
        widget=forms.HiddenInput(),
    )

    count = forms.IntegerField(
        widget=forms.NumberInput(),
        initial=1
    )


class UserAddressForm(forms.ModelForm):
    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='شهر'
    )
    street = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='خیابان'
    )
    alley = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='کوچه'
    )
    number = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label='پلاک'
    )
    unit = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label='واحد'
    )
    mobile = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label='تلفن'
    )

    class Meta:
        model = UserAddress
        fields = [
            'city',
            'street',
            'alley',
            'number',
            'unit',
            'mobile'
        ]
