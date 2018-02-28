from django.contrib import  admin
from django.urls import path
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from hw.views import (
GiftlistView, GiftView, InvitationView, GuestView, GiftNameView,
GiftSearchView, ControlView
)

urlpatterns = [
    path("", csrf_exempt(ControlView.as_view())),
    path('control/', csrf_exempt(ControlView.as_view()), name="control"),
    path('gift_list/', GiftlistView.as_view(), name="gift_list"),
    path('gift/', GiftView.as_view(), name="gift"),
    path('gift/<name>/', GiftNameView.as_view(), name="gift_name"),
    path('guest/', GuestView.as_view(), name="guest"),
    path('guest/<name>/', GuestView.as_view(), name="guest_name"),
    path('gift/search/<query>/', GiftSearchView.as_view(), name="gift_search")
]
