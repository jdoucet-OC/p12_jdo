from django.urls import include, path
from rest_framework_nested import routers
from . import views

client_router = routers.SimpleRouter()
client_router.register(r'clients', views.ClientsViewSet)

event_router = routers.NestedSimpleRouter(client_router, r'clients',
                                          lookup='client')
event_router.register(r'events', views.EventsViewSet,
                      basename='events')

urlpatterns = [
    path('support/', include(client_router.urls)),
    path('support/', include(event_router.urls)),
]
