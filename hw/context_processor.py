from django.urls import reverse
from hw.models import Event, Invitation, Guest, Confirmation, Gift

def guests_data(request):
    guests = Guest.objects.all()
    return {'guests': guests}

def gifts_data(request):
    gifts = Gift.objects.all()
    return {'gifts': gifts}

def invitations_data(request):
    invitations = Invitation.objects.all()
    return {'invitations': invitations}
