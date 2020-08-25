from django import forms
from testapp.models import input_movie


class Input_Form(forms.ModelForm):
    class Meta:
        model = input_movie
        fields = '__all__'

