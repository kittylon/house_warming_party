from django.db import models
from django.utils import timezone


class Invitation(models.Model):
    guest = models.CharField(max_length=200, default='Invitadillo')
    descr = models.TextField()
    link = models.CharField(max_length=200)
    event_date = models.DateTimeField(
            blank=True, null=True)
    place = models.CharField(max_length=200, default='h2m')

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
