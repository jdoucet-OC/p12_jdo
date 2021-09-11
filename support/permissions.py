from rest_framework import permissions
from management.models import Client, Contract, Event, Employee


class ReadOnly(permissions.BasePermission):
    """"""
    def has_object_permission(self, request, view, obj):
        """"""
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return False


class IsAssigned(permissions.BasePermission):
    """"""
    def has_object_permission(self, request, view, obj):
        """"""
        if request.method in permissions.SAFE_METHODS:
            return True
        elif Employee.objects.get(user=request.user).role == "support":
            try:
                supportcontact = obj.supportContact.user
            except AttributeError:
                return False
            return supportcontact == request.user
        else:
            return False
