from .serializers import (ClientSerializer, ContractSerializer,
                          EventSerializer)
from management.models import Client, Contract, Event, Employee
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status
from .permissions import IsContact


class ClientsViewSet(viewsets.ModelViewSet):
    """"""
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated, IsContact]
    queryset = Client.objects.all()

    def create(self, request, *args, **kwargs):
        """"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            employee = Employee.objects.get(user=self.request.user)
            client = serializer.save(salesContact=employee)
            self.check_object_permissions(request, client)
            client.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        self.check_object_permissions(request, instance)
        serializer = self.get_serializer(instance, data=request.data,
                                         partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ContractsViewSet(viewsets.ModelViewSet):
    """"""
    serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticated, IsContact]

    def get_queryset(self):
        """"""
        clientid = self.kwargs['clients_pk']
        client = Client.objects.get(id=clientid)
        return Contract.objects.filter(client=client)

    def create(self, request, *args, **kwargs):
        """"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            clientid = self.kwargs['clients_pk']
            client = Client.objects.get(id=clientid)
            self.check_object_permissions(request, client)
            employee = Employee.objects.get(user=self.request.user)
            contract = serializer.save(client=client,
                                       salesContact=employee)
            contract.save()
            event = Event(contract=contract)
            event.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class EventsViewSet(viewsets.ModelViewSet):
    """"""
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, IsContact]

    def get_queryset(self):
        """"""
        contractid = self.kwargs['contract_pk']
        clientid = self.kwargs['clients_pk']
        client = Client.objects.get(id=clientid)
        contract = Contract.objects.get(id=contractid)
        if client == contract.client:
            return Event.objects.filter(contract=contract)
