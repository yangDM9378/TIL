from django import forms
from .models import Question,Comment

class QuestionForm(forms.ModelForm):
    issue_a=forms.CharField(label='RedTeam')
    issue_b=forms.CharField(label='BlueTeam')
    class Meta:
        model=Question
        fields='__all__'

class CommentForm(forms.ModelForm):

    class Meta:
        model=Comment
        exclude = ('question',)