from django.urls import path
from .views import agregar_al_carrito, ver_carrito, eliminar_del_carrito, iniciar_pago, pago_exitoso
from . import views
from .views import polera_list_cliente



urlpatterns = [
    path('agregar_al_carrito/<int:polera_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('ver_carrito/', ver_carrito, name='ver_carrito'),
    path('agregar_al_carrito/', agregar_al_carrito, name='agregar_al_carrito'),
    path('iniciar_pago/<int:item_id>/', iniciar_pago, name='iniciar_pago'),
    path('pago_exitoso/', pago_exitoso, name="pago_exitoso"),
    path('carrito/eliminar/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('poleras/', views.polera_list_cliente, name='poleras_cliente'),  # Esta es la URL que necesitas
    path('iniciar_pago/', iniciar_pago, name='iniciar_pago'), 

    ]
