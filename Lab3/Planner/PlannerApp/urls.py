from django.urls import path
from .views import SignUpView, LoginView, UserTasksView, CreateTaskView, TaskUpdateView, TaskDetailsView, CompleteTaskView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='api-signup'),
    path('login/', LoginView.as_view(), name='api-login'),
    path('tasks/<str:date>/', UserTasksView.as_view(), name='user_tasks_by_date'),
    path('create_task/', CreateTaskView.as_view(), name='create-task'),
    path('edit_task/', TaskUpdateView.as_view(), name='edit_task'),
    path('task/<int:task_id>/', TaskDetailsView.as_view(), name='task_details'),
    path('complete_task/', CompleteTaskView.as_view(), name='complete_task'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
