from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
import logging
from . import utils


def login_user(request):
    try:
        if request.method == "POST":
            username_or_email = request.POST["username"]
            password = request.POST["password"]
            remember_me = "rememberMe" in request.POST.keys()
            user = authenticate(request, username=username_or_email, password=password)
            if user is not None:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
                return redirect('index')
            else:
                try:
                    username = User.objects.get(email=username_or_email.lower()).username
                    user = authenticate(request, username=username, password=password)
                except User.DoesNotExist:
                    user = None
                if user is not None:
                    login(request, user)
                    if not remember_me:
                        request.session.set_expiry(0)
                    return redirect('index')
                else:
                    messages.success(request, "There Was An Error Logging In, Try Again")
                    return redirect('login')
        else:
            return render(request, 'CoinsMarketLogin/login.html', {})
    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.error('Exception in login view: ', e)
        return render(request, 'CoinsMarketLogin/login.html', {})


def signup_user(request):
    try:
        if request.method == "POST":
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]
            val_result = utils.validate_signup_info(username, password, email)
            if val_result != "":
                messages.success(request, val_result)
                return redirect('signup')
            User.objects.create_user(username, email, password)
            messages.success(request, "Account created")
            return redirect('login')
        else:
            return render(request, 'CoinsMarketLogin/signup.html', {})
    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.error('Exception in signup view: ', e)
        return render(request, 'CoinsMarketLogin/signup.html', {})
