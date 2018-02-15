from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.invitation_list, name='invitation_list'),
    url(r'^invitation/(?P<pk>\d+)/$', views.invitation_detail, name='invitation_detail'),
]
