from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            # Envía el correo electrónico
            send_mail(
                f'Mensaje de contacto de {nombre}',
                mensaje,
                email,
                ['denisse.marion.99@gmail.com'],  # correo donde llegara
            )
            return redirect('home.html')
    else:
        form = ContactForm()
    return render(request, 'contacto.html', {'form': form})
