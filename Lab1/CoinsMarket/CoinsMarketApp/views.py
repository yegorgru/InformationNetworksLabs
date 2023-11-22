from django.shortcuts import render, redirect
import logging
from . import utils
from django.contrib import messages


def index(request):
    if request.user.is_authenticated:
        return render(request, 'CoinsMarketApp/index.html')
    else:
        return redirect('login')


def account(request):
    try:
        if request.method == "POST":
            logger = logging.getLogger(__name__)
            logger.error('Unexpected post request in account view')
        else:
            user = request.user
            return render(request, 'CoinsMarketApp/account.html', {'user': user})
    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.error('Exception in account view: ', e)
        return render(request, 'CoinsMarketLogin/login.html', {})


def edit_account(request):
    try:
        if request.method == "POST":
            user = request.user
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]
            val_result = utils.validate_edit_info(user, username, password, email)
            if val_result != "" and not (val_result == "Password should be at least 8 characters long" and password == ""):
                messages.success(request, val_result)
                return redirect('edit_account')
            if password != "":
                user.set_password(password)
            user.username = username
            user.email = email
            user.save()
            messages.success(request, "Account info updated")
            return redirect('index')
        else:
            user = request.user
            return render(request, 'CoinsMarketApp/edit_account.html', {'user': user})
    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.error('Exception in edit account view: ', e)
        return render(request, 'CoinsMarketLogin/login.html', {})


def manage_balance(request):
    user = request.user
    return render(request, 'CoinsMarketApp/manage_balance.html', {'user': user})
