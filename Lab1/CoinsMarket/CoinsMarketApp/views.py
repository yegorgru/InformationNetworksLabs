from django.shortcuts import render, redirect
import logging
from . import utils
from django.contrib import messages
from . import models
from . import forms


def index(request):
    if request.user.is_authenticated:
        coins = models.Coin.objects.filter(owner=request.user.id)
        for coin in coins:
            print(coin.image_obverse)
        return render(request, 'CoinsMarketApp/index.html', {'coins': coins})
    else:
        return redirect('login')


def account(request):
    try:
        if request.method == "POST":
            logger = logging.getLogger(__name__)
            logger.error('Unexpected post request in account view')
        else:
            user = request.user
            try:
                user_account = models.Account.objects.get(id=user.id)
            except models.Account.DoesNotExist:
                user_account = models.Account(id=user.id, balance=0)
                user_account.save()
            return render(request, 'CoinsMarketApp/account.html', {'user': user, 'user_account': user_account})
    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.error('Exception in account view: ', e)
        return render(request, 'CoinsMarketApp/account.html', {})


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
        return render(request, 'CoinsMarketApp/edit_account.html', {})


def manage_balance(request):
    try:
        if request.method == "POST":
            user = request.user
            try:
                user_account = models.Account.objects.get(id=user.id)
            except models.Account.DoesNotExist:
                user_account = models.Account(id=user.id, balance=0)
                user_account.save()
            try:
                change = int(request.POST["balance_change"])
            except TypeError:
                messages.success(request, "Incorrect amount value")
                return redirect('manage_balance')
            if change < 0:
                messages.success(request, "Negative amount value")
                return redirect('manage_balance')
            curr_balance = user_account.balance
            if "add" in request.POST.keys():
                curr_balance += change
            elif "withdraw" in request.POST.keys():
                if curr_balance < change:
                    messages.success(request, "Not enough money on balance")
                    return redirect('manage_balance')
                else:
                    curr_balance -= change
            user_account.balance = curr_balance
            user_account.save()
            messages.success(request, "Successful balance operation")
            return redirect('manage_balance')
        else:
            user = request.user
            try:
                user_account = models.Account.objects.get(id=user.id)
            except models.Account.DoesNotExist:
                user_account = models.Account(id=user.id, balance=0)
                user_account.save()
            return render(request, 'CoinsMarketApp/manage_balance.html', {'user_account': user_account})
    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.error('Exception in manage balance view: ', e)
        return render(request, 'CoinsMarketApp/manage_balance.html', {})


def new_coin(request):
    try:
        if request.method == "POST":
            form = forms.CreateCoinForm(request.POST, request.FILES)
            if form.is_valid():
                coin_instance = form.save(commit=False)
                coin_instance.owner = request.user.id
                coin_instance.save()
                messages.success(request, "Coin created")
                return redirect('index')
            else:
                logger = logging.getLogger(__name__)
                for field, errors in form.errors.items():
                    logger.error(f"Field: {field}, Errors: {', '.join(errors)}")
                messages.success(request, "Error in form")
                return redirect('new_coin')
        else:
            form = forms.CreateCoinForm()
            return render(request, 'CoinsMarketApp/new_coin.html', {'form': form})
    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.error('Exception in new coin view: ', e)
        return render(request, 'CoinsMarketApp/new_coin.html', {})


def edit_coin(request, coin_id):
    try:
        if request.method == "POST":
            coin = models.Coin.objects.get(pk=coin_id)
            form = forms.CreateCoinForm(request.POST, request.FILES, instance=coin)
            if form.is_valid():
                if "save" in request.POST.keys():
                    coin.save()
                elif "delete" in request.POST.keys():
                    models.Coin.objects.get(pk=coin_id).delete()
                messages.success(request, "Operation successful")
                return redirect('index')
            else:
                logger = logging.getLogger(__name__)
                for field, errors in form.errors.items():
                    logger.error(f"Field: {field}, Errors: {', '.join(errors)}")
                messages.success(request, "Error in form")
                return render(request, 'CoinsMarketApp/view_coin.html', {'form': form})
        else:
            coin = models.Coin.objects.get(pk=coin_id)
            form = forms.CreateCoinForm(instance=coin)
            return render(request, 'CoinsMarketApp/view_coin.html', {'form': form, 'coin': coin})
    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.error('Exception in edit coin view: ', e)
        return render(request, 'CoinsMarketApp/index.html', {})