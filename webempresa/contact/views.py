from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto", # asunto
                f"De {name} <{email}>\n\nEscribió:\n\n{content}", # cuerpo
                "no-contestar@inbox.mailtrap.io", # email origen
                ["ppgreen272@gmail.com", "mejiagreen.jose@gmail.com"], # email destino
                reply_to=[email] # reply to
            )
            try:
                email.send()
                return redirect(reverse('contact') + '?ok')
                
            except: # Algo no ha salido bien
                return redirect(reverse('contact') + '?wr')

    return render(request, "contact/contact.html", {'form':contact_form})
