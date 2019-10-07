from django.conf import settings
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from address.models import Address


class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = PhoneNumberField()
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
