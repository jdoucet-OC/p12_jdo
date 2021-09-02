from django.urls import include, path
from rest_framework_nested import routers
from . import views

client_router = routers.SimpleRouter()
client_router.register(r'clients', views.ClientsViewSet)

contract_router = routers.NestedSimpleRouter(client_router, r'clients',
                                             lookup='client')
contract_router.register(r'contracts', views.ContractsViewSet,
                         basename='contracts')

event_router = routers.NestedSimpleRouter(contract_router, r'contracts',
                                          lookup='contract')
event_router.register(r'events', views.EventsViewSet,
                      basename='events')

urlpatterns = [
    path('sales/', include(client_router.urls)),
    path('sales/', include(contract_router.urls)),
    path('sales/', include(event_router.urls)),
]
