from rest_framework import viewsets
from rest_framework import permissions

from register.serializers import ContractorSerializer, ContractSerializer, FractionSerializer, RegistrySerializer, \
    CarNumberSerializer, RecordSerializer
from register.models import Contractor, Contract, CarNumber, Fraction, Registry, Record


class ContractorViewSet(viewsets.ModelViewSet):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    # permission_classes = [permissions.IsAuthenticated]


class CarNumberViewSet(viewsets.ModelViewSet):
    queryset = CarNumber.objects.all()
    serializer_class = CarNumberSerializer
    # permission_classes = [permissions.IsAuthenticated]


class FractionViewSet(viewsets.ModelViewSet):
    queryset = Fraction.objects.all()
    serializer_class = FractionSerializer
    # permission_classes = [permissions.IsAuthenticated]


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    # permission_classes = [permissions.IsAuthenticated]


class RegistryViewSet(viewsets.ModelViewSet):
    queryset = Registry.objects.all()
    serializer_class = RegistrySerializer
    # permission_classes = [permissions.IsAuthenticated]
