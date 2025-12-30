# 📝 To-Do List Application (Django + Raw SQL)

A simple To-Do List web application built using Django, raw SQL (SQLite), and RESTful APIs, with a minimal UI rendered using templates that consume the APIs via HTTP.

This project is implemented as part of a technical assignment and intentionally avoids Django ORM and generic viewsets.

---

## 📌 Features

- Create, retrieve, update, and delete tasks via REST APIs
- Tasks include:
  - Title
  - Description
  - Due date
  - Status (`PENDING`, `DONE`)
- UI built using HTML + CSS
- UI interacts only via API endpoints (no direct DB access)
- Raw SQL used for database operations
- Basic automated tests using `pytest`

---

## 🛠 Tech Stack

- **Backend:** Django
- **Database:** SQLite (raw SQL, no ORM)
- **Frontend:** HTML, CSS, JavaScript (Fetch API)
- **Testing:** pytest, pytest-django

---

## 📂 Project Structure
```
todo_app/
├── manage.py
├── todo_app/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── tasks/
│   ├── views.py        # API + template views
│   ├── db.py           # Raw SQL database logic
│   ├── urls.py
│   ├── tests/
│   │   └── test_api.py
├── templates/
│   └── tasks/
│       ├── list.html   # Task list UI (API-driven)
│       └── add.html    # Add task UI (API-driven)
└── README.md
```

---

## 🗄 Database Design

The `tasks` table is created automatically at application startup using raw SQL.
```sql
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    due_date TEXT,
    status TEXT DEFAULT 'PENDING'
);
```

### Important Notes

- No Django models are used for task management
- No migrations are created for the `tasks` table
- Django default migrations are applied only for built-in apps (`auth`, `admin`, etc.)

---

## 🔌 API Endpoints

### Create Task
```http
POST /api/tasks/
```

**Request (JSON):**
```json
{
  "title": "Sample Task",
  "description": "Optional description",
  "due_date": "2025-01-31",
  "status": "PENDING"
}
```

---

### List Tasks
```http
GET /api/tasks/
```

---

### Get Single Task
```http
GET /api/tasks/<id>/
```

---

### Update Task
```http
PUT /api/tasks/<id>/
```

**Request (JSON):**
```json
{
  "status": "DONE"
}
```

---

### Delete Task
```http
DELETE /api/tasks/<id>/
```

---

## 🖥 Web Interface (Templates)

- `/` → Task list (home page)
- `/add/` → Add new task

### UI Characteristics

- Centered, responsive layout
- Status badge (`PENDING` / `DONE`)
- Due date displayed
- "Mark Done" action calls PUT API
- Delete action calls DELETE API
- UI uses JavaScript `fetch()` to consume APIs
- No direct database or backend coupling

---

## 🧪 Testing

Automated API tests are implemented using `pytest`.

### Run Tests
```bash
pytest
```

### Coverage

- Create task
- Retrieve tasks
- Update task
- Delete task
- Error handling (404 cases)

---

## ⚙ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone <repo-url>
cd todo_app
```

### 2️⃣ Create Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations (Django internal apps only)
```bash
python manage.py migrate
```

### 5️⃣ Start Server
```bash
python manage.py runserver
```

### 6️⃣ Access Application

Open your browser and navigate to:
```
http://127.0.0.1:8000/
```

---

## 🧠 Design Decisions

- **No ORM:** Raw SQL used to demonstrate database fundamentals
- **No Generic ViewSets:** Function-based views for clarity
- **API-First UI:** Templates consume APIs via HTTP, simulating real-world frontend/backend separation
- **CSRF Disabled for APIs:** APIs are designed for programmatic access
- **CSRF Not Required for UI:** UI uses APIs, not Django form submissions

---

## 🚀 Deployment Note

The application can be temporarily deployed (e.g., Render, Railway, EC2) for demonstration purposes if required.

---

## ✅ Assignment Compliance Checklist

- ✔ CRUD APIs implemented
- ✔ Raw SQL used (no ORM)
- ✔ Templates implemented
- ✔ Templates integrated via APIs
- ✔ Logging & exception handling
- ✔ Automated tests included
- ✔ Clear documentation

---

## 👤 Author

**Yogendra Rajput**  
Python / Backend Developer

---