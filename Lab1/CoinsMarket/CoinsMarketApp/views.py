from django.shortcuts import render, redirect
import logging
from . import utils
from django.contrib import messages
from . import models
from . import forms
from django.contrib.auth.models import User


def index(request):
    if request.user.is_authenticated:
        coins = models.Coin.objects.filter(owner=request.user.id)
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
            curr_password = request.POST["curr_password"]
            if not user.check_password(curr_password):
                messages.success(request, "Incorrect password provided")
                return redirect('edit_account')
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
            if coin.owner != request.user.id:
                return redirect('index')
            form = forms.CreateCoinForm(instance=coin)
            return render(request, 'CoinsMarketApp/view_coin.html', {'form': form, 'coin': coin})
    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.error('Exception in edit coin view: ', e)
        return render(request, 'CoinsMarketApp/index.html', {})


def search(request):
    try:
        if request.method == "POST":
            form = forms.CreateCoinForm(request.POST)
            if form.is_valid():
                if "composite" in request.POST.keys():
                    coins = models.Coin.objects.exclude(owner=request.user.id)
                    if "par_min" in request.POST.keys() and request.POST['par_min'] != '':
                        coins = coins.filter(par__gte=int(request.POST["par_min"]))
                    if "par_max" in request.POST.keys() and request.POST['par_max'] != '':
                        coins = coins.filter(par__lte=int(request.POST["par_max"]))
                    if 'currency' in form.cleaned_data and form.cleaned_data['currency'] != '':
                        coins = coins.filter(currency__exact=form.cleaned_data["currency"])
                    if "year_min" in request.POST.keys() and request.POST['year_min'] != '':
                        coins = coins.filter(year__gte=int(request.POST["year_min"]))
                    if "year_max" in request.POST.keys() and request.POST['year_max'] != '':
                        coins = coins.filter(year__lte=int(request.POST["year_max"]))
                    if 'material' in form.cleaned_data and form.cleaned_data['material'] != '':
                        coins = coins.filter(material__exact=form.cleaned_data["material"])
                    if "weight_min" in request.POST.keys() and request.POST['weight_min'] != '':
                        coins = coins.filter(weight__gte=float(request.POST["weight_min"]))
                    if "weight_max" in request.POST.keys() and request.POST['weight_max'] != '':
                        coins = coins.filter(weight__lte=float(request.POST["weight_max"]))
                    if "diameter_min" in request.POST.keys() and request.POST['diameter_min'] != '':
                        coins = coins.filter(diameter__gte=float(request.POST["diameter_min"]))
                    if "diameter_max" in request.POST.keys() and request.POST['diameter_max'] != '':
                        coins = coins.filter(diameter__lte=float(request.POST["diameter_max"]))
                    if "price_min" in request.POST.keys() and request.POST['price_min'] != '':
                        coins = coins.filter(price__gte=int(request.POST["price_min"]))
                    if "price_max" in request.POST.keys() and request.POST['price_max'] != '':
                        coins = coins.filter(price__lte=int(request.POST["price_max"]))
                    if 'description' in form.cleaned_data and form.cleaned_data['description'] != '':
                        coins = coins.filter(description__contains=form.cleaned_data["description"])
                else:
                    coins_general = models.Coin.objects.exclude(owner=request.user.id)
                    coins = models.Coin.objects.none()
                    if request.POST['par_min'] != '' and request.POST['par_max'] != '':
                        coins = coins.union(coins_general.filter(par__gte=int(request.POST["par_min"]), par__lte=int(request.POST["par_max"])))
                    elif request.POST['par_min'] != '':
                        coins = coins.union(coins_general.filter(par__gte=int(request.POST["par_min"])))
                    elif request.POST['par_max'] != '':
                        coins = coins.union(coins_general.filter(par__lte=int(request.POST["par_max"])))
                    if 'currency' in form.cleaned_data and form.cleaned_data['currency'] != '':
                        coins = coins.union(coins_general.filter(currency__exact=form.cleaned_data["currency"]))
                    if request.POST['year_min'] != '' and request.POST['year_max'] != '':
                        coins = coins.union(coins_general.filter(year__gte=int(request.POST["year_min"]), year__lte=int(request.POST["year_max"])))
                    elif request.POST['year_min'] != '':
                        coins = coins.union(coins_general.filter(year__gte=int(request.POST["year_min"])))
                    elif request.POST['year_max'] != '':
                        coins = coins.union(coins_general.filter(year__lte=int(request.POST["year_max"])))
                    if 'material' in form.cleaned_data and form.cleaned_data['material'] != '':
                        coins = coins.union(coins_general.filter(material__exact=form.cleaned_data["material"]))
                    if request.POST['weight_min'] != '' and request.POST['weight_max'] != '':
                        coins = coins.union(coins_general.filter(weight__gte=float(request.POST["weight_min"]), weight__lte=float(request.POST["weight_max"])))
                    elif request.POST['weight_min'] != '':
                        coins = coins.union(coins_general.filter(weight__gte=float(request.POST["weight_min"])))
                    elif request.POST['weight_max'] != '':
                        coins = coins.union(coins_general.filter(weight__lte=float(request.POST["weight_max"])))
                    if request.POST['diameter_min'] != '' and request.POST['diameter_max'] != '':
                        coins = coins.union(coins_general.filter(diameter__gte=float(request.POST["diameter_min"]), diameter__lte=float(request.POST["diameter_max"])))
                    elif request.POST['diameter_min'] != '':
                        coins = coins.union(coins_general.filter(diameter__gte=float(request.POST["diameter_min"])))
                    elif request.POST['diameter_max'] != '':
                        coins = coins.union(coins_general.filter(diameter__lte=float(request.POST["diameter_max"])))
                    if request.POST['price_min'] != '' and request.POST['price_max'] != '':
                        coins = coins.union(coins_general.filter(price__gte=int(request.POST["price_min"]), price__lte=int(request.POST["price_max"])))
                    elif request.POST['price_min'] != '':
                        coins = coins.union(coins_general.filter(price__gte=int(request.POST["price_min"])))
                    elif request.POST['price_max'] != '':
                        coins = coins.union(coins_general.filter(price__lte=int(request.POST["price_max"])))
                    if 'description' in form.cleaned_data and form.cleaned_data['description'] != '':
                        coins = coins.union(coins_general.filter(description__contains=form.cleaned_data["description"]))
                form = forms.CreateCoinForm()
                return render(request, 'CoinsMarketApp/search.html', {'form': form, 'coins': coins})
            else:
                logger = logging.getLogger(__name__)
                for field, errors in form.errors.items():
                    logger.error(f"Field: {field}, Errors: {', '.join(errors)}")
                form = forms.CreateCoinForm()
                return render(request, 'CoinsMarketApp/search.html', {'form': form})
        else:
            form = forms.CreateCoinForm()
            return render(request, 'CoinsMarketApp/search.html', {'form': form})
    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.error('Exception in search coin view: ', e)
        form = forms.CreateCoinForm()
        return render(request, 'CoinsMarketApp/search.html', {'form': form})


def search_coin(request, coin_id):
    try:
        if request.method == "POST":
            coin = models.Coin.objects.get(pk=coin_id)
            price = coin.price
            user = request.user
            try:
                user_account = models.Account.objects.get(id=user.id)
            except models.Account.DoesNotExist:
                user_account = models.Account(id=user.id, balance=0)
                user_account.save()
            curr_balance = user_account.balance
            if curr_balance < price:
                messages.success(request, "Not enough money on balance")
                coin = models.Coin.objects.get(pk=coin_id)
                user = User.objects.get(id=coin.owner)
                return render(request, 'CoinsMarketApp/search_coin.html', {'coin': coin, 'owner': user.username})
            else:
                curr_balance -= price
            user_account.balance = curr_balance
            user_account.save()
            try:
                owner_user_account = models.Account.objects.get(id=coin.owner)
            except models.Account.DoesNotExist:
                owner_user_account = models.Account(id=coin.owner, balance=0)
                owner_user_account.save()
            curr_balance = owner_user_account.balance + price
            owner_user_account.balance = curr_balance
            owner_user_account.save()
            coin.owner = user.id
            coin.save()
            messages.success(request, "Successful buy")
            return redirect('index')
        else:
            coin = models.Coin.objects.get(pk=coin_id)
            user = User.objects.get(id=coin.owner)
            return render(request, 'CoinsMarketApp/search_coin.html', {'coin': coin, 'owner': user.username})
    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.error('Exception in search coin view: ', e)
        return redirect('search')
