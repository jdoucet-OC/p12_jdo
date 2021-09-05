from rest_framework import serializers
from management.models import Client, Contract, Event


class ClientSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = Client
        fields = ['id', 'firstName', 'lastName', 'email',
                  'phone', 'companyName', 'dateCreated',
                  'dateUpdated', 'salesContact']


class ContractSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = Contract
        fields = ['id', 'salesContact', 'dateCreated', 'client',
                  'dateUpdated', 'status', 'amount', 'paymentDue']


class EventSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = Event
        fields = ['id', 'supportContact', 'client',
                  'dateCreated', 'dateUpdated', 'eventStatus',
                  'attendees', 'eventDate', 'notes']
