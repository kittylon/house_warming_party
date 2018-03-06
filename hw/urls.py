from django.contrib import  admin
from django.urls import path
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from hw.views import (
GiftlistView, GiftView, InvitationView,
GiftSearchView, ControlView, GuestStuffView, ConfirmationView
)

urlpatterns = [
    path("", csrf_exempt(ControlView.as_view())),
    path('control/', csrf_exempt(ControlView.as_view()), name="control"),
    path('gift_list/', GiftlistView.as_view(), name="gift_list"),
    path('gift/', GiftView.as_view(), name="gift"),
    path('gift/search/<query>/', GiftSearchView.as_view(), name="gift_search"),
    path('confirmation/<int:query>/', ConfirmationView.as_view(), name="confirmation"),
    path('invitation/<int:query>/', csrf_exempt(GuestStuffView.as_view()), name="guest_stuff")
]
