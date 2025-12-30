# tasks/urls.py
from django.urls import path
from .views import tasks_api, task_detail_api, task_list_view, task_add_view

urlpatterns = [
    # API
    path("api/tasks/", tasks_api),
    path("api/tasks/<int:task_id>/", task_detail_api),

    # UI
    path("", task_list_view, name="task_list"),
    path("add/", task_add_view, name="task_add"),
]
