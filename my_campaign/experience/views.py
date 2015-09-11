from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import  login as login_auth
from django.contrib.auth import logout as logout_auth

def criar_usuario(request):
    usuario = User.objects.create_user("marcio", "marcio@email.com", "senha")
    print('Usuário criado com sucesso!')