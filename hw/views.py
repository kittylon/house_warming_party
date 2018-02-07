from django.shortcuts import render
from .models import Invitation

# Create your views here.
def invitation_list(request):
    invitations = Invitation.objects.all()
    return render(request, 'hw/invitation_list.html', {'invitations': invitations})
