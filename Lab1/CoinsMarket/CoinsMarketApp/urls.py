from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account', views.account, name='account'),
    path('edit_account', views.edit_account, name='edit_account'),
    path('manage_balance', views.manage_balance, name='manage_balance'),
]
