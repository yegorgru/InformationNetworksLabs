from django.contrib import admin
from django.urls import path, include

from frontend.views import index_view

urlpatterns = [
    path('', index_view, name='index'),
    path('home/', include('frontend.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('PlannerApp.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
