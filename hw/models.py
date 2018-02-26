from django.db import models
from django.utils import timezone

class Event(models.Model):
    name = models.CharField(max_length=50, default='Fiesta')
    date = models.DateTimeField(blank=True, null=False)
    place = models.URLField()
    host = models.CharField(max_length=50, default='Carolina')

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Invitation(models.Model):
    descr = models.TextField()
    event = models.ForeignKey(Event,models.SET_NULL,blank=True,null=True)
    active = models.BooleanField(default=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.descr

class Guest(models.Model):
    name = models.CharField(max_length=70)
    mail = models.EmailField(max_length=254)
    mobile = models.IntegerField()
    active = models.BooleanField(default=True)
    invitation = models.ForeignKey(Invitation,models.SET_NULL,blank=True,null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Confirmation(models.Model):
    STATUS_CHOICES = (('Going','Y'), ('Not going','N'))

    status = models.CharField(max_length=11, choices=STATUS_CHOICES)
    active = models.BooleanField(default=True)
    invitation = models.ForeignKey(Invitation, models.SET_NULL,blank=True,null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.invitation

class Gift(models.Model):
    STATUS_CHOICES = (('Available','A'), ('Taken','T'))

    name = models.CharField(max_length=200)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    price = models.DecimalField(max_digits=8, decimal_places=3)
    pic = models.ImageField()
    active = models.BooleanField(default=True)
    slug = models.SlugField(default="gift")
    confirmation = models.ForeignKey(Confirmation, models.SET_NULL,blank=True,null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class ConfirmationDetail(models.Model):
    confirmation = models.ForeignKey(Confirmation, models.SET_NULL, blank=True, null=True)
    gift = models.ForeignKey(Gift, models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.confirmation
