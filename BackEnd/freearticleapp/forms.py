from django import forms
from django.forms import ModelForm

from freearticleapp.models import FreeArticle


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable',
                                                           'style': 'text-align : left;'
                                                                    'min-height : 10rem'}))
    class Meta:
        model = FreeArticle
        fields = ['title','image','content']


class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')