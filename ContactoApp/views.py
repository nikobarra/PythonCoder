from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.
def contacto (request):
    formulario_contacto = ContactForm()
    
    if request.method == 'POST':
        formulario_contacto=ContactForm(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get('name')
            apellido=request.POST.get('last_name')
            email=request.POST.get('email')
            contenido=request.POST.get('content')
            
            """ el correo seteado abajo es a donde llegaran los mails """
            email = EmailMessage('Mensaje desde Web', "el usuario {} {} con correo {} dice:\n\n {}" .format(nombre, apellido, email, contenido), "",["nikodread1979@gmail.com"], reply_to=[email])
            try:
                email.send()
                return redirect("/Contacto/?correcto")
            except: 
                return redirect("/Contacto/?incorrecto")
            
    return render(request, 'ContactoApp/contacto.html', {'formContact':formulario_contacto})