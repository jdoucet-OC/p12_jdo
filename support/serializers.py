from rest_framework import serializers
from management.models import Client, Contract, Event


class ClientSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = Client
        fields = ['id', 'firstName', 'lastName', 'email',
                  'phone', 'companyName', 'dateCreated',
                  'dateUpdated', 'salesContact']


class EventSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = Event
        fields = ['id', 'supportContact', 'client',
                  'dateCreated', 'dateUpdated', 'eventStatus',
                  'attendees', 'eventDate', 'notes']
