from django.db import models
from django.utils import timezone

class Person(models.Model):
    role = models.CharField(max_length=50, default='Guest')
    name = models.CharField(max_length=70)
    mail = models.EmailField(max_length=254)
    mobile = models.IntegerField(max_length=15)

    def publish(self):
        self.save()

class Event(models.Model):
    name = models.CharField(max_length=50, default='Fiesta')
    date = models.DateTimeField(blank=True, null=False))
    place = models.URLField()

    def publish(self):
        self.save()

class Invitation(models.Model):
    descr = models.TextField()

    def publish(self):
        self.save()

class Confirmacion(models.Model):
    status = models.CharField(max_length=200)
    invitation = models.ForeignKey(Invitation, on_delete=models.,)

    def publish(self):
        self.save()

class Gift(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=3)

    def publish(self):
        self.save()
