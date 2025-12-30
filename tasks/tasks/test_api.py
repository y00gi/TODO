import json
import pytest
from django.test import Client

@pytest.mark.django_db
class TestTaskAPI:

    def setup_method(self):
        self.client = Client()

    def test_create_task(self):
        response = self.client.post(
            "/api/tasks/",
            data=json.dumps({
                "title": "Test Task",
                "description": "Test Desc",
                "due_date": "2025-01-31"
            }),
            content_type="application/json"
        )

        assert response.status_code == 201
        assert "id" in response.json()

    def test_get_tasks(self):
        self.client.post(
            "/api/tasks/",
            data=json.dumps({"title": "Task 1"}),
            content_type="application/json"
        )

        response = self.client.get("/api/tasks/")
        assert response.status_code == 200
        assert isinstance(response.json()["data"], list)

    def test_get_single_task(self):
        create = self.client.post(
            "/api/tasks/",
            data=json.dumps({"title": "Single Task"}),
            content_type="application/json"
        )
        task_id = create.json()["id"]

        response = self.client.get(f"/api/tasks/{task_id}/")
        assert response.status_code == 200
        assert response.json()["title"] == "Single Task"

    def test_update_task(self):
        create = self.client.post(
            "/api/tasks/",
            data=json.dumps({"title": "Old Title"}),
            content_type="application/json"
        )
        task_id = create.json()["id"]

        response = self.client.put(
            f"/api/tasks/{task_id}/",
            data=json.dumps({"title": "New Title", "status": "DONE"}),
            content_type="application/json"
        )

        assert response.status_code == 200

    def test_delete_task(self):
        create = self.client.post(
            "/api/tasks/",
            data=json.dumps({"title": "To Delete"}),
            content_type="application/json"
        )
        task_id = create.json()["id"]

        response = self.client.delete(f"/api/tasks/{task_id}/")
        assert response.status_code == 204

    def test_404_on_missing_task(self):
        response = self.client.get("/api/tasks/9999/")
        assert response.status_code == 404
