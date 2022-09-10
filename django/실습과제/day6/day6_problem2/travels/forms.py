from django import forms
from .models import travels

class TravelsForm(forms.ModelForm):
    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ex)제주도',
            }
        )
    )

    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'placeholder': 'ex)2022-02-22',
            }
        ),
    )
    end_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'placeholder': 'ex)2022-02-22',
            }
        ),
    )
    class Meta():
        model=travels
        fields='__all__'