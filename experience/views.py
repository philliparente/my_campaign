# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Campaign

from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'experience/index.html')


@login_required
def campaigns(request):
    if request.POST and request.POST['username']:

        user = User.objects.filter(username=request.POST['username'])
        campaigns = Campaign.objects.filter(author=user)

        return render(request, 'experience/campaigns.html', {'campaigns': campaigns})

    else:

        return render(request, 'experience/index.html', {'message': 'Não existem campanhas para esse usuário'})


def campaign(request, campaign_id):
    pass


def contributors(request):
    return render(request, 'experience/contributors.html')


def auth_login(request):
    message = ''

    if request.user.is_authenticated():
        return render(request, 'experience/mypage.html', {})

    if request.POST:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])

        if user is not None:
            # the password verified for the user
            if user.is_active:
                login(request, user)
                message = "User is valid, active and authenticated"
                return render(request, 'experience/mypage.html', {'message': message})
            else:
                message = "The password is valid, but the account has been disabled!"
        else:
            # the authentication system was unable to verify the username and password
            message = "The username and password were incorrect."

    return render(request, 'experience/login.html', {'message': message})


def signup(request):
    message = ''
    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        try:
            User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            message = 'Usuário salvo com sucesso'
        except:
            message = 'Erro ao salvar usuário'

    return render(request, 'experience/signup.html', {'message': message})


def auth_logout(request):
    logout(request)
    return redirect(reverse("experience:index"))
