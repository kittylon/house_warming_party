from django.shortcuts import render
from .models import Invitation, Gift
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.list import ListView

#not using function anymore, we use views instead (platzi)
class HomeView(TemplateView):
    template_name = 'hw/home.html'

class GiftView(TemplateView):
    template_name = 'hw/gift.html'

class GiftNameView(TemplateView):
    template_name = 'hw/gift_name.html'

class GuestView(TemplateView):
    template_name = 'hw/guest.html'

class InvitationView(TemplateView):
    template_name = 'hw/invitation_detail.html'

class GiftSearchView(ListView):
    template_name = "hw/gift_search.html"
    model = Gift

    def get_queryset(self):
        query = self.kwargs['query']
        return Gift.objects.filter(price__lte=query)
