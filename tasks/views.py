# tasks/views.py
import json
import logging
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from .db import create_task, get_all_tasks, get_task_by_id, update_task, delete_task
from django.shortcuts import render

logger = logging.getLogger(__name__)


@csrf_exempt
def tasks_api(request):
    try:
        if request.method == "GET":
            tasks = get_all_tasks()
            return JsonResponse({"data": tasks}, status=200)

        if request.method == "POST":
            body = json.loads(request.body)

            if "title" not in body or not body["title"]:
                return JsonResponse(
                    {"error": "title is required"}, status=400
                )

            task_id = create_task(
                title=body["title"],
                description=body.get("description"),
                due_date=body.get("due_date"),
                status=body.get("status", "PENDING"),
            )

            return JsonResponse(
                {"message": "Task created", "id": task_id},
                status=201,
            )

        return HttpResponseNotAllowed(["GET", "POST"])

    except Exception as e:
        logger.exception("Error in tasks_api")
        return JsonResponse({"error": "Internal server error"}, status=500)

@csrf_exempt
def task_detail_api(request, task_id):
    try:
        if request.method == "GET":
            task = get_task_by_id(task_id)
            if not task:
                return JsonResponse({"error": "Task not found"}, status=404)
            return JsonResponse(task, status=200)

        if request.method == "PUT":
            body = json.loads(request.body)

            updated = update_task(
                task_id=task_id,
                title=body.get("title"),
                description=body.get("description"),
                due_date=body.get("due_date"),
                status=body.get("status"),
            )

            if not updated:
                return JsonResponse(
                    {"error": "Task not found or no fields to update"},
                    status=400,
                )

            return JsonResponse({"message": "Task updated"}, status=200)

        if request.method == "DELETE":
            deleted = delete_task(task_id)
            if not deleted:
                return JsonResponse({"error": "Task not found"}, status=404)

            return JsonResponse({"message": "Task deleted"}, status=204)

        return HttpResponseNotAllowed(["GET", "PUT", "DELETE"])

    except Exception:
        logger.exception("Error in task_detail_api")
        return JsonResponse({"error": "Internal server error"}, status=500)

def task_list_view(request):
    return render(request, "tasks/list.html")

def task_add_view(request):
    return render(request, "tasks/add.html")