from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    address_one = models.CharField(max_length=100, null=True, blank=True)
    address_two = models.CharField(max_length=100, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    landmark = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    pincode = models.CharField(max_length=50, null=True, blank=True)
    phonenumber = models.CharField(max_length=20, null=True, blank=True)
    phonenumber_two = models.CharField(max_length=20, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.user.username
