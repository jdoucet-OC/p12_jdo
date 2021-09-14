from .serializers import (ClientSerializer,
                          EventSerializer)
from management.models import Client, Event, Contract
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status
from .permissions import IsAssigned, ReadOnly


class ClientsViewSet(viewsets.ModelViewSet):
    """"""
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated, ReadOnly]
    queryset = Client.objects.all()


class EventsViewSet(viewsets.ModelViewSet):
    """"""

    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, IsAssigned]

    def get_queryset(self):
        """"""
        clientid = self.kwargs['client_pk']
        client = Client.objects.get(id=clientid)
        contracts = Contract.objects.filter(client=client)
        return Event.objects.filter(contract__in=contracts)

    def update(self, request, *args, **kwargs):
        """"""
        instance = self.get_object()
        self.check_object_permissions(request, instance)
        contractpk = instance.contract.pk
        request.data._mutable = True
        request.data['contract'] = contractpk
        request.data._mutable = False
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
