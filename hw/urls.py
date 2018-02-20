from django.contrib import  admin
from django.urls import path
from hw.views import (
HomeView, GiftsView, InvitationView, GuestView
)

#djangogirls
# from django.conf.urls import url
# from . import views


urlpatterns = [
    path("", HomeView.as_view()),
    path('home/', HomeView.as_view()),
    path('gift/', GiftsView.as_view()),
    path('guest/', GuestView.as_view()),
    # path('invitation/<guest>', InvitationView.as_view())
]
