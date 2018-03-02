from django.shortcuts import render
from .models import Invitation, Gift, Guest
from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.decorators.csrf import csrf_protect,csrf_exempt
import json
from django.core.exceptions import ObjectDoesNotExist

#not using function anymore, we use views instead (platzi)
class GiftlistView(TemplateView):
    template_name = 'hw/gift_list.html'

class GiftView(TemplateView):
    template_name = 'hw/gift.html'

class InvitationView(TemplateView):
    template_name = 'hw/invitation_detail.html'
    model = Invitation

class GiftSearchView(ListView):
    template_name = "hw/gift_search.html"
    model = Gift

    def get_queryset(self):
        query = self.kwargs['query']
        return Gift.objects.filter(price__lte=query)

class GuestStuffView(ListView):
    template_name = "hw/guest_stuff.html"
    model = Guest

    def get_queryset(self):
        query = self.kwargs['query']
        return Guest.objects.filter(pk=query)

    def post(self, request, *args, **kwargs):
        dict_ids = json.loads(request.body.decode('utf-8'))
        gift_id = dict_ids['gift_id']
        guest_id = dict_ids['guest_id']
        guest = get_object_or_404(Guest, pk=guest_id)
        gift = get_object_or_404(Gift, pk=gift_id)
        gift.status = 'Taken'
        gift.guest = guest
        gift.save(update_fields=['status', 'guest'])
        response = {'status': 0, 'message': 'Gift added!' }
        return HttpResponse(json.dumps(response), content_type='application/json')

class ControlView(TemplateView):
    template_name = "hw/control.html"

    def post(self, request, *args, **kwargs):
        print('....................................')
        dict_mail = json.loads(request.body.decode('utf-8'))
        mail = dict_mail['mail']
        guest = get_object_or_404(Guest, mail=mail)
        url = '/invitation/' + str(guest.pk)
        response = {'status': 0, 'url': url }
        return HttpResponse(json.dumps(response), content_type='application/json')
