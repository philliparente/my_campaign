from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^campaign/(?P<campaign_id>[0-9]+)$', views.campaign, name='campaign'),
    url(r'^$', views.index, name='index'),
]