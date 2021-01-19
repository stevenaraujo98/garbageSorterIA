from django import forms

class ImageForm(forms.Form):
    imagen = forms.ImageField()

class DataForm(forms.Form):
    net = forms.CharField()