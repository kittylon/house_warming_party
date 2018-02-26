from django.contrib import  admin
from django.urls import path
from hw.views import (
HomeView, GiftView, InvitationView, GuestView, GiftNameView,
GiftSearchView
)

#djangogirls
# from django.conf.urls import url
# from . import views


urlpatterns = [
    path("", HomeView.as_view()),
    path('home/', HomeView.as_view(), name="home"),
    path('gift/', GiftView.as_view(), name="gift"),
    path('gift/<name>/', GiftNameView.as_view(), name="gift_name"),
    path('guest/', GuestView.as_view(), name="guest"),
    path('guest/<name>/', GuestView.as_view(), name="guest_name"),
    path('gift/search/<query>/', GiftSearchView.as_view(), name="gift_search")
]
