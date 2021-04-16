from django.shortcuts import render, HttpResponse

# Create your views here.

def Corintias(request,numero1, numero2, result):
    result = numero1 + numero2
    return HttpResponse('<h1>O resultado desta soma  {} + {} = {}</h1>' .format(numero1, numero2, result))
def Juquia(request,n1,op,n2,resultado):
    if op == '-':
        resultado = n1 - n2
    elif op == '+':
        resultado = n1 + n2
    elif op == '*':
        resultado = n1 * n2
    elif op == '/':
        resultado = n1 / n2

    return HttpResponse('<h1>Calculadora: {}  {}  {} = {}</h1>' .format(n1, op, n2, resultado))

# def Juquia(request):
#     return HttpResponse('<h1>Chama Papai</h1>')