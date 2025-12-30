# Project Structure & Implementation Details

## Database Setup

- Django default migrations are applied only for built-in apps (auth, admin, sessions, contenttypes).
- The `tasks` table is created automatically at application startup using raw SQL.
- No Django ORM models or migrations are used for task management.

---

## File-wise Explanation

### `tasks/db.py`

**Purpose:** Database access layer (raw SQL only)

- Manages SQLite connection
- Creates tasks table at startup
- Handles all database operations (insert, select, update, delete)
- Uses parameterized queries to avoid SQL injection

**Key responsibilities:**
- `get_connection()`
- `create_tasks_table()`
- `create_task(...)`
- `get_all_tasks()`
- (optional) update / delete helpers

---

### `tasks/apps.py`

**Purpose:** Application initialization

- Calls `create_tasks_table()` inside `AppConfig.ready()`
- Ensures the tasks table exists before handling any request
- Avoids migrations and ORM usage

---

### `settings.py`

**Purpose:** Application configuration

- Registers the app using: `tasks`
- Uses SQLite database (`db.sqlite3`) via Django settings
- No model registration for the tasks app

---

### `tasks/views.py`

**Purpose:** API endpoints and template views

**Contains:**
- RESTful API views for task CRUD operations
- Template-rendering views for UI

**Responsibilities:**
- Parse and validate request data
- Call database functions from `db.py`
- Return JSON responses with proper HTTP status codes
- Render HTML templates for task listing and creation
- No ORM, serializers, or generic viewsets are used

---

### `tasks/urls.py`

**Purpose:** URL routing

**Defines routes for:**
- API endpoints (`/api/tasks/`)
- Web interface (`/tasks/`, `/tasks/add/`)
- Keeps API and UI routes cleanly separated

---

### `tasks/templates/tasks/`

**Purpose:** User Interface (HTML templates)

**Includes:**
- `list.html` – Displays the list of tasks
- `add.html` – Form for adding a new task
- Templates interact with the backend via API endpoints

---

### `tasks/tests/test_api.py`

**Purpose:** Automated testing

- Uses `pytest` and `pytest-django`
- Covers API endpoints:
  - Create task
  - Retrieve tasks
- Verifies response status codes and JSON structure

---

### `manage.py`

**Purpose:** Django project entry point

- Used for running the server
- Used for applying Django default migrations

---

## API Documentation (Summary)

### `POST /api/tasks/`

Creates a new task

**Request body (JSON):**
```json
{
  "title": "Sample Task",
  "description": "Task description",
  "due_date": "2025-01-31",
  "status": "PENDING"
}
```

### `GET /api/tasks/`

Returns list of all tasks

---

## Design Decisions

- Raw SQL was used intentionally to comply with the assignment constraint of not using ORM.
- Database logic is isolated in `db.py` to maintain separation of concerns.
- Application startup table creation avoids manual DB setup steps.
- Django templates are integrated with API endpoints for UI interactions.

---

## Notes

- No Django models, serializers, or generic viewsets are used.
- Logging and exception handling are implemented at the view level.
- The application can be temporarily deployed for demonstration if required.