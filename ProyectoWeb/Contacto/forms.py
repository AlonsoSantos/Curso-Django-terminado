from django import forms

class formularioContacto(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True, max_length=100)
    email = forms.EmailField(label='Email', required=True, max_length=100)
    contenido = forms.CharField(widget=forms.Textarea(), label='Contenido', required=True) 