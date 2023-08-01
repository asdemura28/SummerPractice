from django.db import models


class Contractor(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Fraction(models.Model):
    fraction = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.fraction


class CarNumber(models.Model):
    number = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return self.number


class Contract(models.Model):
    number = models.CharField(max_length=20)
    date = models.DateField()
    contractor = models.ForeignKey(Contractor, on_delete=models.PROTECT)

    def __str__(self):
        return self.number


class Record(models.Model):
    date = models.DateField()
    contractor = models.ForeignKey(Contractor, on_delete=models.PROTECT)
    car_number = models.ForeignKey(CarNumber, on_delete=models.PROTECT)
    driver_name = models.CharField(max_length=50)
    fraction = models.ForeignKey(Fraction, on_delete=models.PROTECT)
    weight = models.IntegerField()


class Registry(models.Model):
    contractor = models.ForeignKey(Contractor, on_delete=models.PROTECT)
    contract = models.ForeignKey(Contract, on_delete=models.PROTECT)
    date_begin = models.DateField()
    date_end = models.DateField(blank=True, null=True)

    def __str__(self):
        return 'Реестр_' + self.contractor.title

    