from django import forms
from .models import Institucion, Inscrito

class InstitucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = '__all__'



class InscritoForm(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = '__all__'
