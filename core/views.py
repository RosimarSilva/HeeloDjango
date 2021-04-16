from django.shortcuts import render, HttpResponse

# Create your views here.

def Corintias(request,numero1, numero2, result):
    result = numero1 + numero2
    return HttpResponse('<h1>O resultado desta soma  {} + {} = {}</h1>' .format(numero1, numero2, result))
