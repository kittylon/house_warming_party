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

    guests = [guest1, guest2]

    return {'guests': guests}

def gifts_data(request):
    gift1 = {'name': 'silla para comedor', 'status': 'libre', 'price': 80, 'confirmation': 'Ok'}
    gift2 = {'name': 'silla para comedor', 'status': 'libre', 'price': 80, 'confirmation': 'Ok'}
    gift3 = {'name': 'organizador de cubiertos', 'status': 'libre', 'price': 40, 'confirmation': 'Ok'}

    gifts = [gift1, gift2, gift3]

    return {'gifts': gifts}

def invitations_data(request):
    invitation1 = {'descr': 'Hola, paji, dame regalos', 'event': 'HW PARTY BABY!'}
    invitation2 = {'descr': 'Hola, Moni, no me des regalos', 'event': 'HW PARTY BABY!'}
    invitation3 = {'descr': 'Hola, Joha, trae comida', 'event': 'HW PARTY BABY!'}

    invitations = [invitation1, invitation2, invitation3]

    return {'invitations': invitations}
