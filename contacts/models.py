from django.conf import settings
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from shop.models.address import BaseShippingAddress, ISO_3166_CODES


class Contact(models.Model):
    first = models.CharField(max_length=200)
    last = models.CharField(max_length=200)
    phone = PhoneNumberField()
    address_

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
