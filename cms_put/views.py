from django.shortcuts import render
from models import Pages
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.

def mostrar(request, recurso):
  if (request.method == "GET"):
    try:
      fila = Pages.objects.get(name = recurso)
      return HttpResponse (request.method + " HOLA " + str(fila.id) + " " + fila.name + " " + fila.page)
    except Pages.DoesNotExist:
      return HttpResponseNotFound('Page not found '+ recurso)
    except Pages.MultipleObjectsReturned:
      return HttpResponseNotFound('Recuso '+ recurso + ' repetido elimine los duplicados de la tabla')
  elif(request.method == "PUT"):
      entrada = Pages(name = recurso, page = request.body)
      entrada.save()
      return HttpResponse ("Agregado " + recurso + " con valor: " + request.body)
    

