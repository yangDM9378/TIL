from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    genre_a='co'
    genre_b='rhd'
    genre_c='ro'
    GENRE_CHOICES=[(genre_a,'코미디'),(genre_b,'공포'),(genre_c,'로맨스')]
    genre=forms.ChoiceField(choices=GENRE_CHOICES)
    
    score=forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'min':0,
                'max':5,
                'step':0.5
            }
        )
    )

    release_date=forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type':'date'
            }
        )
    )
    class Meta:
        model=Movie
        fields='__all__'