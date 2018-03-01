from django.contrib import admin
from .models import Invitation
from .models import Guest
from .models import Gift

admin.site.register(Invitation)
admin.site.register(Guest)
admin.site.register(Gift)
