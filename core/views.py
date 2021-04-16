from django.shortcuts import render, HttpResponse

# Create your views here.

def Corintias(request,name, idade):
    return HttpResponse('<h1>O palmeiras não tem {} e nem {} copinha</h1>' .format(name, idade))
