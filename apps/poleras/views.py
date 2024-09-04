from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Polera
from .forms import PoleraForm
from datetime import datetime

# Vista Clase para que solo los administradores puedan acceder al CRUD Polera
# Esta clase debe ir incluida en la clase PoleraList,PoleraCreate,PoleraUpdate y PoleraDelete
class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser
    
# Vista Clase Listar Poleras
class PoleraList(AdminRequiredMixin, ListView):     
    model = Polera
    template_name = 'Polera/polera_list.html'

# Vista Clase Crear Polera
class PoleraCreate(AdminRequiredMixin, CreateView):
    model = Polera
    form_class = PoleraForm
    template_name = 'Poleras/polera_form.html'
    success_url = reverse_lazy('polera_list')

# Vista Clase Actualizar Polera
class PoleraUpdate(AdminRequiredMixin, UpdateView):
    model = Polera
    form_class = PoleraForm
    template_name = 'Poleras/polera_form.html'
    success_url = reverse_lazy('polera_list')

# Vista Clase Borrar Poleras
class PoleraDelete(AdminRequiredMixin, DeleteView):
    model = Polera
    template_name = 'Poleras/polera_borrar.html'
    success_url = reverse_lazy('polera_list')

#------------
#Vista Lista Poleras (CLIENTE)
class PoleraListCliente(ListView):
    model = Polera
    template_name = 'Poleras/polera_list_cliente.html'  
    context_object_name = 'poleras_cliente'  
    
    def post(self, request, *args, **kwargs):
        form = PoleraForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data


