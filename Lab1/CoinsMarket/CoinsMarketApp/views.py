from django.shortcuts import render, redirect


def index(request):
    if request.user.is_authenticated:
        return render(request, 'CoinsMarketApp/index.html')
    else:
        return redirect('login')
