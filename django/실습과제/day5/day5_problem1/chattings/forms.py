from django import forms
from .models import Chat

class ChatForm(forms.ModelForm):
    user=forms.CharField(
        label='작성자',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Nickname',
            }
        )
    )

    content=forms.CharField(
        label='내용',
        widget=forms.Textarea(
             attrs={
                'placeholder':'Chat!',
            }
        ),
    )
    
    class Meta:
        model=Chat
        fields='__all__'