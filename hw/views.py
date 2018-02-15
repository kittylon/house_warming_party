from django.shortcuts import render
from .models import Invitation
from django.shortcuts import render, get_object_or_404

# Create your views here.
def invitation_list(request):
    invitations = Invitation.objects.all()
    return render(request, 'hw/invitation_list.html', {'invitations': invitations})

def invitation_detail(request, pk):
    invitation = get_object_or_404(Invitation, pk=pk)
    return render(request, 'hw/invitation_detail.html',{'invitation': invitation})
