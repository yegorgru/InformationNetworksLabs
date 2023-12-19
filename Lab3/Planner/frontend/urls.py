from django.urls import path
from .views import login_view, index_view, signup_view


urlpatterns = [
    path('', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
]
