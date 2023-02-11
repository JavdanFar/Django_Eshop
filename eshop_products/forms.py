from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'لطفا نام خود را وارد کنید', 'class': 'form-control'}),
        label='نام'
    )
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'لطفا نظر خود را وارد کنید', 'class': 'form-control'}),
        label='نظر'
    )

    class Meta:
        model = Comment
        fields = [
            'name',
            'comment'
        ]
