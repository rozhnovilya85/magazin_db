from django.shortcuts import render

# Create your views here.

from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from .filters import ShopFilter
from .models import City, Street, Magazine
from .serializers import CitySerializer, StreetSerializer, ShopSerializer


class CityAPIView(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    @action(methods=['get'], detail=True)
    def street(self, request, pk=None):
        city = City.objects.get(pk=pk)
        street = Street.objects.filter(city=city).values_list('id', 'name')
        return Response(street)


class ShopAPIView(ListCreateAPIView):
    queryset = Magazine.objects.all()
    serializer_class = ShopSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ShopFilter





