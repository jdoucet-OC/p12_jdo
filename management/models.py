from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    """"""
    roles = [('sales', 'Sales'),
             ('management', 'Management'),
             ('support', 'Support')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=roles)

    def __str__(self):
        return f"{self.user.last_name}, {self.user.first_name}"


class Client(models.Model):
    """"""
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    companyName = models.CharField(max_length=250)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)
    salesContact = models.ForeignKey(to=Employee,
                                     on_delete=models.SET_NULL,
                                     null=True)

    def __str__(self):
        return f"{self.lastName}, {self.firstName}"


class Contract(models.Model):
    """"""
    salesContact = models.ForeignKey(to=Employee,
                                     on_delete=models.SET_NULL,
                                     null=True)
    client = models.ForeignKey(to=Client,
                               on_delete=models.CASCADE,
                               null=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField()
    paymentDue = models.DateTimeField()


class Event(models.Model):
    """"""
    supportContact = models.ForeignKey(to=Employee,
                                       on_delete=models.SET_NULL,
                                       null=True)
    client = models.ForeignKey(to=Client,
                               on_delete=models.CASCADE)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)
    eventStatus = models.ForeignKey(to=Contract,
                                    on_delete=models.CASCADE)
    attendees = models.IntegerField()
    eventDate = models.DateTimeField()
    notes = models.TextField(max_length=2048)
