from django.contrib import admin
from .models import Event
from .models import Invitation
from .models import Person
from .models import Confirmation
from .models import Gift

admin.site.register(Event)
admin.site.register(Invitation)
admin.site.register(Person)
admin.site.register(Confirmation)
admin.site.register(Gift)
