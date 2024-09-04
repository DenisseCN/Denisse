from django.urls import path
from .views import agregar_al_carrito, ver_carrito, eliminar_del_carrito, iniciar_pago, pago_exitoso

urlpatterns = [
    path('agregar_al_carrito/<int:polera_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('ver_carrito/', ver_carrito, name='ver_carrito'),
    path('eliminar_del_carrito/<int:item_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('agregar_al_carrito/', agregar_al_carrito, name='agregar_al_carrito'),
    path('iniciar_pago/<int:item_id>/', iniciar_pago, name='iniciar_pago'),
    path('pago_exitoso/', pago_exitoso, name="pago_exitoso"),
]
