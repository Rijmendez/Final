from django.shortcuts import render

# Create your views here.
def menu (request):
    return render(request,'page/menu.html')

def consulta (request) :
    return render(request, 'consulta.html')

def producto (request) :
    return render(request, 'producto.html')

def Factura (request) :
    return render(request, 'page/Facturacion.html')