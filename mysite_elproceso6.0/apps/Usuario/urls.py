from django.urls import path, include
from . import views
from .views import RegistroUsuario, UserList, logout_view, UsuarioAPI, listar_usuarios, UsuarioRetrieveUpdateDestroy, UsuarioCreate, UsuarioUpdate, UsuarioDelete


urlpatterns = [
    path('registrar', RegistroUsuario.as_view(),name="registrar_usuario"),
    path('listar', UserList.as_view(), name="listar_usuario"),
    path('logout/', logout_view, name='logout'),
    path('listar_usuarios/', listar_usuarios, name='listar_usuarios'),

    # PATH RELACIONADO A API
    path('api/usuarios/', UsuarioAPI.as_view(), name='usuarios_api'),
    path('api/usuarios/<int:pk>/', UsuarioRetrieveUpdateDestroy.as_view(), name='usuario_detail'),
    path('api/usuarios/create/', UsuarioCreate.as_view(), name='usuario_create'),
    path('api/usuarios/update/<int:pk>/', UsuarioUpdate.as_view(), name='usuario_update'),
    path('api/usuarios/delete/<int:pk>/', UsuarioDelete.as_view(), name='usuario_delete'),
    
]
