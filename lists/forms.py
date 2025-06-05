from django import forms
from .models import MovieList

class MovieListForm(forms.ModelForm):
    class Meta:
        model = MovieList
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
