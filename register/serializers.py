from register.models import Contractor, Contract, Registry, CarNumber, Fraction, Record
from rest_framework import serializers


class ContractorSerializer(serializers.HyperlinkedModelSerializer):
    # id = serializers.IntegerField()
    # title = serializers.CharField()

    class Meta:
        model = Contractor
        fields = ['id', 'title']


class ContractSerializer(serializers.HyperlinkedModelSerializer):
    contractor = serializers.PrimaryKeyRelatedField(queryset=Contractor.objects.all())

    def create(self, validated_data):
        return Contract.objects.create(**validated_data)

    class Meta:
        model = Contract
        fields = ['id', 'number', 'date', 'contractor']


class CarNumberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarNumber
        fields = ['id', 'number']


class FractionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fraction
        fields = ['id', 'fraction']


class RecordSerializer(serializers.HyperlinkedModelSerializer):
    contractor = serializers.PrimaryKeyRelatedField(queryset=Contractor.objects.all())
    car_number = serializers.PrimaryKeyRelatedField(queryset=CarNumber.objects.all())
    fraction = serializers.PrimaryKeyRelatedField(queryset=Fraction.objects.all())

    class Meta:
        model = Record
        fields = ['id', 'contractor', 'fraction', 'car_number', 'weight', 'date', 'driver_name']


class RegistrySerializer(serializers.HyperlinkedModelSerializer):
    contractor = ContractorSerializer(read_only=True)
    contract = ContractSerializer(read_only=True)

    class Meta:
        model = Registry
        fields = ['id', 'contractor', 'contract', 'date_begin', 'date_end']
