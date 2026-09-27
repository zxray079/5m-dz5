from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Zone, Visitors
from .serializers import ZoneSerializer, VisitorsSerializer


class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = ['location']
    search_fields = ['location']
    ordering_fields = ['location', 'created_at']
    ordering = ['-created_at']


class VisitorsViewSet(viewsets.ModelViewSet):
    queryset = Visitors.objects.all()
    serializer_class = VisitorsSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = ['zone', 'is_allowed']
    search_fields = ['name', 'information']
    ordering_fields = ['name', 'created_at']
    ordering = ['-created_at']