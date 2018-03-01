from django.contrib import  admin
from django.urls import path
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from hw.views import (
GiftlistView, GiftView, InvitationView, GiftNameView,
GiftSearchView, ControlView, GuestStuffView
)

urlpatterns = [
    path("", csrf_exempt(ControlView.as_view())),
    path('control/', csrf_exempt(ControlView.as_view()), name="control"),
    path('gift_list/', GiftlistView.as_view(), name="gift_list"),
    path('gift/', GiftView.as_view(), name="gift"),
    path('gift/<name>/', GiftNameView.as_view(), name="gift_name"),
    path('gift/search/<query>/', GiftSearchView.as_view(), name="gift_search"),
    path('invitation/<int:query>/', GuestStuffView.as_view(), name="guest_stuff")
]
