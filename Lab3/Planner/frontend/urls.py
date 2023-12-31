from django.urls import path
from .views import login_view, index_view, signup_view, create_task, task


urlpatterns = [
    path('', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('create_task/', create_task, name='create_task'),
    path('task/<int:task_id>/', task, name='task'),
]
