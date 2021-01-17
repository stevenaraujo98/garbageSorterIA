from django import forms

class ImageForm(forms.Form):
    imagen = forms.ImageField()