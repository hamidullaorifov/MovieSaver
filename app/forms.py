from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}))
    class Meta:
        model = Movie 
        fields = '__all__'
        # fields = ('name','date','description','picture','video')


