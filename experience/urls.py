from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^campaign/(?P<campaign_id>[0-9]+)/$', views.campaign, name='campaign'),
]