from django.shortcuts import render


def login_view(request):
    return render(request, 'login.html')


def signup_view(request):
    return render(request, 'signup.html')


def index_view(request):
    return render(request, 'index.html')


def create_task(request):
    return render(request, 'create_task.html')
