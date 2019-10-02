from django.conf import settings
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

class ShippingAddress(models.Model):
    name = models.CharField(
        "Full name",
        max_length=1024,
    )

    address1 = models.CharField(
        "Address line 1",
        max_length=1024,
    )

    address2 = models.CharField(
        "Address line 2",
        max_length=1024,
    )

    zip_code = models.CharField(
        "ZIP / Postal code",
        max_length=12,
    )

    city = models.CharField(
        "City",
        max_length=1024,
    )

    country = CountryField()

    class Meta:
        verbose_name = "Shipping Address"
        verbose_name_plural = "Shipping Addresses"


class AddressModelMixin(models.Model):
    name = models.CharField(
        "Full name",
        max_length=1024,
    )

    address1 = models.CharField(
        "Address line 1",
        max_length=1024,
    )
    # other fields

    class Meta:
        abstract = True


class BillingAddress(models.Model, AddressModelMixin):
    tax_number = models.CharField(
        "Tax number",
        max_length=50,
    )

    class Meta:
        verbose_name = "Billing Address"
        verbose_name_plural = "Billing Addresses"
