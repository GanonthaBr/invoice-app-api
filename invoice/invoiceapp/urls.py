from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet, ClientViewSet, DesignationViewSet

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)
router.register(r'clients',ClientViewSet)
router.register(r'designations',DesignationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]