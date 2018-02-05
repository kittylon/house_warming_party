from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.invitation_list, name='invitation_list'),
]
