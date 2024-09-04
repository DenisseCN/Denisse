from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from .forms import RegistroForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import logout, login
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import generics, status # type: ignore
from rest_framework.permissions import IsAuthenticated, IsAdminUser # type: ignore

from .serializers import UsuarioSerializer

import requests # type: ignore

class RegistroUsuario(CreateView):
    model = User 
    template_name = "Usuario/registrar.html"
    form_class = RegistroForm 
    success_url = reverse_lazy('home') 

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)  
        return response

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
 
class UserList(ListView):
    model = User
    template_name = 'Usuario/listar_usuario.html'

def logout_view(request):
    logout(request)
    return redirect('home')

# <----------- API CODE ------------->
#-------------------------------------

# OBTENER DATOS DE USUARIOS
class UsuarioAPI(APIView):
    def get(self, request):
        usuarios = User.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)
    
# LISTAR USUARIOS
def listar_usuarios(request):
    try:
        response = requests.get('http://localhost:8000/api/usuarios/')
        response.raise_for_status()
        
        # PASARLO A JSON
        usuarios_api = response.json()

    #CONTROL DE ERRORES
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud a la API: {e}")
        usuarios_api = []

    #RETORNAR AL TEMPLATE USANDO LA LLAVE: usuarios_api 
    return render(request, 'Usuario/listar_usuarios.html', {'usuarios_api': usuarios_api})



# CRUD CREAR, ELIMINAR, MODIFICAR USUARIO

class UsuarioRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioCreate(APIView):

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioUpdate(APIView):
    def put(self, request, pk):
        usuario = User.objects.get(pk=pk)
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioDelete(APIView):

    def delete(self, request, pk):
        usuario = User.objects.get(pk=pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)