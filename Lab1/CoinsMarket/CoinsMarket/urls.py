from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from CoinsMarketApp.views import index

urlpatterns = [
    path('', index, name='index'),
    path('home/', include('CoinsMarketApp.urls')),
    path('login/', include('django.contrib.auth.urls')),
    path('login/', include('CoinsMarketLogin.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
