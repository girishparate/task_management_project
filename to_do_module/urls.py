from django.urls import path
from .views import TaskDashboardView, TaskCRUDView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('task-dashboard', login_required(TaskDashboardView.as_view()), name='task-dashboard'),

    path('task-details/<pk>', login_required(TaskCRUDView.as_view()), name='task-details'),

    path('task-delete-edit/<pk>', login_required(TaskCRUDView.as_view()), name='task-delete-edit')
]