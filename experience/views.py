# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from django.http import HttpResponse
from django.shortcuts import render
from .models import Campaign


def index(request):
    return render(request, 'experience/index.html')


def campaigns(request):
    campaigns = Campaign.objects.all()
    return render(request, 'experience/campaigns.html', {'campaigns': campaigns})


def campaign(request, campaign_id):
    pass


def contributors(request):
    return render(request, 'experience/contributors.html')