from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from examenapp.models import Fabriek
from examenapp.forms import FabriekForm


# View die de homepage laat zien.
def home(request):
    return render(request, 'home/home.html')


# View die de contact pagina laat zien.
def contact(request):
    return render(request, 'home/contact.html')


# View die alle gegevens laat zien in een overzicht.
class fabrieksoverzicht(ListView):
    model = Fabriek
    template_name = 'crud/fabriekenlist.html'


# View waarmee een fabriek aangemaakt kan worden.
class createfabriek(CreateView):
    form_class = FabriekForm
    template_name = 'crud/createfabriek.html'
    success_url = reverse_lazy('fabrieksoverzicht')


# View waarmee een fabriek verwijderd kan worden.
class deletefabriek(DeleteView):
    model = Fabriek
    template_name = 'crud/deletefabriek.html'
    success_url = reverse_lazy('fabrieksoverzicht')


# View waarmee een fabriek gewijzigd kan worden.
class editfabriek(UpdateView):
    model = Fabriek
    form_class = FabriekForm
    template_name = 'crud/editfabriek.html'
    success_url = reverse_lazy('fabrieksoverzicht')
