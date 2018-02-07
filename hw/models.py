from django.db import models
from django.utils import timezone

class Event(models.Model):
    name = models.CharField(max_length=50, default='Fiesta')
    date = models.DateTimeField(blank=True, null=False)
    place = models.URLField()
    host = models.CharField(max_length=50, default='Carolina')

    def publish(self):
        self.save()

class Invitation(models.Model):
    descr = models.TextField()
    event = models.ForeignKey(Event,models.SET_NULL,blank=True,null=True)

    def publish(self):
        self.save()

class Person(models.Model):
    role = models.CharField(max_length=50, default='Invitado')
    name = models.CharField(max_length=70)
    mail = models.EmailField(max_length=254)
    mobile = models.IntegerField(max_length=15)
    invitation = models.ForeignKey(Invitation,models.SET_NULL,blank=True,null=True)

    def publish(self):
        self.save()

class Confirmation(models.Model):
    status = models.CharField(max_length=200)
    invitation = models.ForeignKey(Invitation, models.SET_NULL,blank=True,null=True)

    def publish(self):
        self.save()

class Gift(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=3)
    confirmation = models.ForeignKey(Confirmation, models.SET_NULL,blank=True,null=True)

    def publish(self):
        self.save()
