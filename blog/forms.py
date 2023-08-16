from django import forms
from .models import Article


class ArticleModelForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Title less then 20 words'
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Text area is required'
            }
        )
    )

    class Meta:
        model = Article
        fields = '__all__'
