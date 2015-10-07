# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^campaigns/$', views.campaigns, name='campaign'),
    url(r'^campaign/(?P<campaign_id>[0-9]+)$', views.campaign, name='campaign'),
    url(r'^$', views.index, name='index'),
]