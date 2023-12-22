from rest_framework import generics
from .models import Inscrito, Institucion
from .serializers import InscritoSerializer, InstitucionSerializer
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.http import JsonResponse


def home(request):
    autor_data = {
        'nombre': 'Nataly Peñeipil',
        'Asignatura': 'Programación back-end',
        'rut': '20583603-9',
    }
    return render(request, 'home.html', {'autor_data': autor_data})

class InscritoListCreateView(generics.ListCreateAPIView):
    queryset = Inscrito.objects.all()
    serializer_class = InscritoSerializer
    

class InscritoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inscrito.objects.all()
    serializer_class = InscritoSerializer

class InstitucionListCreateView(generics.ListCreateAPIView):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer

class InstitucionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer


