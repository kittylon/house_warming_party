from django.urls import reverse
def guests_data(request):
    guest1 = {
                'role': 'guest',
                'name': 'Moni',
                'mail': 'monica@hwparty.com',
                'mobile': 3023221899,
                'invitation': 1
              }

    guest2 = {
                'role': 'guest',
                'name': 'Meli',
                'mail': 'meli@hwparty.com',
                'mobile': 3023221899,
                'invitation': 2
             }

    guest3 = {
                'role': 'guest',
                'name': 'Paji',
                'mail': 'paji@hwparty.com',
                'mobile': 3023221899,
                'invitation': 3
             }

    guests = [guest1, guest2, guest3]

    return {'guests': guests}

def gifts_data(request):
    gift1 = {
                'name': 'silla',
                'status': 'libre',
                'price': 80,
                'confirmation': 'Ok',
                'detail_url': reverse("gift_name", kwargs={'name':'silla'})
            }

    gift2 = {
                'name': 'tape',
                'status': 'libre',
                'price': 80,
                'confirmation': 'Ok',
                'detail_url': reverse("gift_name", kwargs={'name':'tape'})
            }
    gift3 = {
                'name': 'organizador',
                'status': 'libre',
                'price': 40,
                'confirmation': 'Ok',
                'detail_url': reverse("gift_name", kwargs={'name':'organizador'})
            }

    gifts = [gift1, gift2, gift3]

    return {'gifts': gifts}

def invitations_data(request):
    invitation1 = {'descr': 'Hola, Moni, no me des regalos', 'event': 'HW PARTY BABY!'}
    invitation2 = {'descr': 'Hola, Meli, dame regalos', 'event': 'HW PARTY BABY!'}
    invitation3 = {'descr': 'Hola, Oaji, trae comida', 'event': 'HW PARTY BABY!'}

    invitations = [invitation1, invitation2, invitation3]

    return {'invitations': invitations}
