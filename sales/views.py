from rest_framework import viewsets, permissions
from .serializers import (ClientSerializer, ContractSerializer,
                          EventSerializer)
from management.models import Client, Contract, Event


class ClientsViewSet(viewsets.ModelViewSet):
    """"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ContractsViewSet(viewsets.ModelViewSet):
    """"""
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class EventsViewSet(viewsets.ModelViewSet):
    """"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
