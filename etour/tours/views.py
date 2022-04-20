from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Tour, Location
from .serializers import TourSerializer, LocationSerializer
from .paginators import TourPaginator


class TourViewSet(viewsets.ViewSet, generics.ListAPIView):#hiện thực sẵn
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    pagination_class = TourPaginator

    def get_queryset(self):
        tours = Tour.objects.filter(active=True)

        q = self.request.query_params.get('q')
        if q is not None:
            tours = tours.filter(name__icontains=q)

        return tours


class LocationViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
