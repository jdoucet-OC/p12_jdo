from rest_framework import viewsets, permissions
from .serializers import (ClientSerializer,
                          EventSerializer)
from management.models import Client, Event


class EventsViewSet(viewsets.ModelViewSet):
    """"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ClientsViewSet(viewsets.ModelViewSet):
    """"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer