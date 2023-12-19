from django.shortcuts import render


def login_view(request):
    return render(request, 'login.html')


def index_view(request):
    return render(request, 'index.html')
