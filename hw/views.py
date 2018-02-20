from django.shortcuts import render
from .models import Invitation
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

#not using function anymore, we use views instead (platzi)
class HomeView(TemplateView):
    template_name = 'hw/home.html'

class GiftsView(TemplateView):
    template_name = 'hw/gifts.html'

class GuestView(TemplateView):
    template_name = 'hw/guests.html'

class InvitationView(TemplateView):
    template_name = 'hw/invitation_detail.html'
