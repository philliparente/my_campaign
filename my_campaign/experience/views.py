from django.http import HttpResponse
from django.shortcuts import render
from .models import Campaign


def index(request):
    campaigns = Campaign.objects.all()
    return render(request, 'experience/index.html', {'campaigns': campaigns})


def campaign(request, campaign_id):
	print campaign_id
	pass
