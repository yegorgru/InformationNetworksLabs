from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account', views.account, name='account'),
    path('edit_account', views.edit_account, name='edit_account'),
    path('manage_balance', views.manage_balance, name='manage_balance'),
    path('new_coin', views.new_coin, name='new_coin'),
    path("edit_coin/<int:coin_id>/", views.edit_coin, name='edit_coin'),
    path("search_coin/<int:coin_id>/", views.search_coin, name='search_coin'),
    path('search', views.search, name='search'),
]
