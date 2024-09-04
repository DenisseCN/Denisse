from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import PoleraList, PoleraCreate, PoleraUpdate, PoleraDelete, PoleraListCliente

urlpatterns = [
    # Paths CRUD
    path('listar_polera/', PoleraList.as_view(), name="polera_list"),
    path('crear_polera/', PoleraCreate.as_view(), name="polera_form"),
    path('editar_polera/<int:pk>/', PoleraUpdate.as_view(), name="polera_update"),
    path('borrar_polera/<int:pk>/', PoleraDelete.as_view(), name="polera_delete"),

    #Path lista polera (cliente)
    path('poleras/', PoleraListCliente.as_view(), name="poleras_cliente"),

    
]

