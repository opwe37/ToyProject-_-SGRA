from django import forms
from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable',
                                                           'style': 'text-align : left;'
                                                                    'min-height : 10rem'}))
    class Meta:
        model = Article
        fields = ['title', 'max_personnel', 'region', 'progress_method', 'content']


class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')