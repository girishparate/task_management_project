from django.urls import path
from .views import TaskDashboardView, TaskCRUDView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('task-dashboard', TaskDashboardView.as_view(), name='task-dashboard'),

    path('task-details/<pk>', TaskCRUDView.as_view(), name='task-details'),

    path('task-delete-edit/<pk>', TaskCRUDView.as_view(), name='task-delete-edit')
]