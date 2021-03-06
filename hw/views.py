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

class ConfirmationView(ListView):
    template_name ="hw/confirmation.html"
    model = Guest
    prev_gifts = 0

    def get_queryset(self):
        query = self.kwargs['query']
        return Guest.objects.filter(pk=query)

class GuestStuffView(ListView):
    template_name = "hw/guest_stuff.html"
    model = Guest

    def get(self, request, *args, **kwargs):
        query = self.kwargs['query']
        object_list =  Guest.objects.filter(pk=query)
        gifts_id = self.count_prev_gifts(query)
        return render(request, self.template_name, { 'gifts_id': gifts_id, 'object_list': object_list} )

    @staticmethod
    def count_prev_gifts(guest_id):
        gifts_id = []
        prev_gifts = Gift.objects.filter(guest_id=str(guest_id))
        for gift in prev_gifts:
            gifts_id.append(gift.pk)
        return gifts_id

    @staticmethod
    def add_gift(guest_id, gifts_to_add):
        guest = get_object_or_404(Guest, pk=guest_id)
        for gift_id in gifts_to_add:
            gift = get_object_or_404(Gift, pk=gift_id)
            if gift.status == 'Available':
                gift.status = 'Taken'
                gift.guest = guest
                gift.save(update_fields=['status', 'guest'])

        return guest.pk

    @staticmethod
    def remove_gift(guest_id, gifts_to_remove):
        guest = get_object_or_404(Guest, pk=guest_id)
        for gift_id in gifts_to_remove:
            gift = get_object_or_404(Gift, pk=gift_id)
            if gift.status == 'Taken' and gift.guest == guest:
                gift.status = 'Available'
                gift.guest = None
                gift.save(update_fields=['status', 'guest'])

        return guest.pk

    def post(self, request, *args, **kwargs):
        dict_ids = json.loads(request.body.decode('utf-8'))
        guest_id = dict_ids['guest_id']
        gifts_to_add = dict_ids['gifts_to_add']
        gifts_to_remove = dict_ids['gifts_to_remove']
        prev_gifts = GuestStuffView.count_prev_gifts(str(guest_id))
        print(prev_gifts)
        GuestStuffView.add_gift(guest_id, gifts_to_add)
        GuestStuffView.remove_gift(guest_id, gifts_to_remove)
        url = '/confirmation/' + str(guest_id)
        response = {'status': 0, 'url': url }
        return HttpResponse(json.dumps(response), content_type='application/json')

class ControlView(TemplateView):
    template_name = "hw/control.html"

    def post(self, request, *args, **kwargs):
        print('....................................')
        dict_mail = json.loads(request.body.decode('utf-8'))
        mail = dict_mail['mail']
        guest = get_object_or_404(Guest, mail=mail)
        gifts = Gift.objects.filter(guest_id=guest).count()

        if gifts > 0:
            url = url = '/confirmation/' + str(guest.pk)
        else:
            url = '/invitation/' + str(guest.pk)

        response = {'status': 0, 'url': url}
        return HttpResponse(json.dumps(response), content_type='application/json')
