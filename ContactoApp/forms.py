from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label=('Nombre'),required=True, max_length=30)
    last_name = forms.CharField(label=('Apellido'),required=True, max_length=30)
    email = forms.CharField(label=('Correo Electronico'),required=True)
    content = forms.CharField (label=('Mensaje'), max_length=200, widget=forms.Textarea(attrs={'rows':10, 'cols':20}))