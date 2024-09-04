from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import CarritoItem, Polera
from django.contrib import messages
from datetime import datetime
from transbank.webpay.webpay_plus.transaction import Transaction, WebpayOptions 
import random
from django.views.decorators.csrf import csrf_exempt
@require_POST
@login_required
def agregar_al_carrito(request):
    
    if request.method == "POST":
        user_instance = request.user
        polera_id = request.POST.get('polera_id')
        talla = request.POST.get('talla')
        cantidad = int(request.POST.get('cantidad'))
        precio = int(request.POST.get('precio'))
        creado_en = datetime.now()
        polera = Polera.objects.get(pk=polera_id)

        # Guardar los cambios en el stock de la polera
        nuevo_item_carrito = CarritoItem(
            user=user_instance,
            polera=polera,
            talla=talla,
            cantidad=cantidad,
            precio=precio,
            creado_en=creado_en
        )

        # Guardar la instancia del modelo en la base de datos
        nuevo_item_carrito.save()

        #{'success': True, 'message': 'Polera agregada al carrito correctamente'})
        
        return redirect('poleras_cliente')




@login_required(login_url='/login/')
def ver_carrito(request):
    carrito_items = CarritoItem.objects.filter(user=request.user)
    return render(request, 'carrito/ver_carrito.html', {'carrito_items': carrito_items})

def home(request):
    context = {
        'is_authenticated': request.user.is_authenticated
    }
    return render(request, 'home.html', context)




@login_required
def eliminar_del_carrito(request, item_id):
    carrito_item = get_object_or_404(CarritoItem, id=item_id, user=request.user)
    carrito_item.delete()
    messages.success(request, 'Producto eliminado del carrito!')
    return redirect('ver_carrito')

#PAGOOOOOOOOOOooooooooooooooooooooo TRANSKBANK
#Tipo de tarjeta   Detalle                        Resultado
#----------------   -----------------------------  ------------------------------
#VISA              4051885600446623
#CVV 123
#cualquier fecha de expiración  Genera transacciones aprobadas.
#AMEX              3700 0000 0002 032
#CVV 1234
#cualquier fecha de expiración  Genera transacciones aprobadas.
# MASTERCARD        5186 0595 5959 0568
# CVV 123
# cualquier fecha de expiración  Genera transacciones rechazadas.
# Redcompra         4051 8842 3993 7763            Genera transacciones aprobadas (para operaciones que permiten débito Redcompra y prepago)
# Redcompra         4511 3466 6003 7060            Genera transacciones aprobadas (para operaciones que permiten débito Redcompra y prepago)
# Redcompra         5186 0085 4123 3829            Genera transacciones rechazadas (para operaciones que permiten débito Redcompra y prepago)


@csrf_exempt
def iniciar_pago(request, item_id):

    # Esta es la implementacion de la VISTA iniciar_pago, que tiene la responsabilidad
    # de iniciar el pago, por medio de WebPay. Lo primero que hace es seleccionar un 
    # número de orden de compra, para poder así, identificar a la propia compra.
    # Como esta tienda no maneja, en realidad no tiene el concepto de "orden de compra"
    # pero se indica igual
    print("Webpay Plus Transaction.create")
    buy_order = str(random.randrange(1000000, 99999999))
    session_id = request.user.username
    amount = Polera.objects.get(pk=item_id).precio
    return_url = 'http://127.0.0.1:8000/pago_exitoso/'

    # response = Transaction.create(buy_order, session_id, amount, return_url)
    commercecode = "597055555532"
    apikey = "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C"

    tx = Transaction(options=WebpayOptions(commerce_code=commercecode, api_key=apikey, integration_type="TEST"))
    response = tx.create(buy_order, session_id, amount, return_url)
    print(response['token'])

    #perfil = PerfilUsuario.objects.get(user=request.user)

    context = {
        "buy_order": buy_order,
        "session_id": session_id,
        "amount": amount,
        "return_url": return_url,
        "response": response,
        "token_ws": response['token'],
        "url_tbk": response['url'],
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "rut": "11111111-1",
        "dirusu": 'Santiago',
    }

    return render(request, "carrito/iniciar_pago.html", context)

@csrf_exempt
def pago_exitoso(request):

    if request.method == "GET":
        token = request.GET.get("token_ws")
        print("commit for token_ws: {}".format(token))
        commercecode = "597055555532"
        apikey = "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C"
        tx = Transaction(options=WebpayOptions(commerce_code=commercecode, api_key=apikey, integration_type="TEST"))
        response = tx.commit(token=token)
        print("response: {}".format(response))

        

        context = {
            "buy_order": response['buy_order'],
            "session_id": response['session_id'],
            "amount": response['amount'],
            "response": response,
            "token_ws": token,
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "dirusu": 'Santiago',
            "response_code": response['response_code']
        }

        return render(request, "carrito/pago_exitoso.html", context)
    else:
        return redirect(ver_carrito)