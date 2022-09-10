from django import forms
from .models import Movies

class MoviesForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': '세 얼간이',
            }
        )
    )
    director = forms.CharField(
        label='감독',
        widget=forms.TextInput(
            attrs={
                'class': 'my-director',
                'placeholder': '라지쿠마르 히라니',
            }
        )
    )
    comment = forms.CharField(
        label='코맨트',
        widget=forms.Textarea(
            attrs={
                'class': 'my-comment',
                'placeholder': '나 얼간이 아니다!',
                'rows': 3,
                'cols': 40,
            }
        ),
        error_messages={
            'required': '내용 입력하라고..',
        }
    )

    class Meta:
        model=Movies
        fields='__all__'