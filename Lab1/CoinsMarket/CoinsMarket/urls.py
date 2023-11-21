from django.contrib import admin
from django.urls import path, include

from CoinsMarketApp.views import index

urlpatterns = [
    path('', index, name='index'),
    path('login/', include('django.contrib.auth.urls')),
    path('login/', include('CoinsMarketLogin.urls')),
    path('admin/', admin.site.urls),
]
