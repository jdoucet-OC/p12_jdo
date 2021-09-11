from rest_framework import permissions
from management.models import Client, Contract, Event, Employee


class IsContact(permissions.BasePermission):
    """"""
    def has_object_permission(self, request, view, obj):
        """"""
        if request.method in permissions.SAFE_METHODS:
            return True
        elif Employee.objects.get(user=request.user).role == "sales":
            if isinstance(obj, Client) or isinstance(obj, Contract):
                salescontact = obj.salesContact.user
                return salescontact == request.user
            if isinstance(obj, Event):
                contract = obj.contract
                salescontact = contract.salesContact.user
                return salescontact == request.user
            else:
                return False
