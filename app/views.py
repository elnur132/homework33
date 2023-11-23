from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import PersonForm
from .models import Person

# Create your views here.
class CreatePerson(CreateView):
    form_class = PersonForm
    template_name = 'create_person.html'
    success_url = reverse_lazy('main')

class ListPerson(ListView):
    model = Person
    template_name = 'list_person.html'
    context_object_name = 'people'