from django.db import models
from django.utils import timezone

class Invitation(models.Model):
    TYPE_CHOICES = (('Giver','G'), ('Single','S'), ('Couple', 'C'))

    inv_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    descr = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.descr

class Guest(models.Model):
    name = models.CharField(max_length=70)
    mail = models.EmailField(max_length=254)
    mobile = models.IntegerField()
    going = models.BooleanField(default=True)
    invitation = models.ForeignKey(Invitation, models.SET_NULL, blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Gift(models.Model):
    STATUS_CHOICES = (('Available','A'), ('Taken','T'))

    name = models.CharField(max_length=200)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, null=False)
    price = models.DecimalField(max_digits=8, decimal_places=3)
    pic = models.TextField()
    guest = models.ForeignKey(Guest, models.SET_NULL, blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
