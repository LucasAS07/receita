from django.shortcuts import render


def cadastro(request):
    return render(request, 'usuarios/cadastro.html')


def login(request):
    return render(request, 'usuarios/login')


def logout(request):
    pass


def dashboard(request):
    pass