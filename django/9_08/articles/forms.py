from django import forms
from .models import Article
# form class
# Model에 없는 값을 입력받고 싶을때

# modelform class
# model에 있는 값만 입력받고 싶을때

class ArticleForm(forms.ModelForm):

    class Meta:
        model=Article
        fields="__all__"
