from django.db import models


class OfficeLocation(models.Model):
    # TODO: Add geo fields like lat and long - GeoDjango
    location_id = models.BigAutoField(primary_key=True)

    address_street = models.CharField(max_length=100, null=False, blank=False)
    address_city = models.CharField(max_length=100, null=False, blank=False)
    address_state = models.CharField(max_length=100, null=False, blank=False)
    address_zipcode = models.CharField(max_length=100, null=False, blank=False)

    phone = models.CharField(max_length=100, null=False, blank=False)


class Vehicle(models.Model):
    pass


class VehicleClass(models.Model):
    class_id = models.BigAutoField(primary_key=True)
    vehicle_class = models.CharField(max_length=100, null=False, blank=False)
    rent_charge = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    extra_charge = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
