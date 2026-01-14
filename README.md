# Todo API - Task Management System

A RESTful API for managing tasks with JWT authentication, built with FastAPI.

## Features

- CRUD operations for tasks
- JWT-based authentication
- Input validation with Pydantic
- Comprehensive error handling
- Auto-generated API documentation (Swagger/OpenAPI)

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file (copy from `.env.example`):
```bash
cp .env.example .env
```

3. Update the `SECRET_KEY` in `.env` with a secure random string:
```bash
openssl rand -hex 32
```

## Running the API

```bash
uvicorn main:app --reload
```

The API will be available at: http://localhost:8000

## API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Authentication
- `POST /auth/register` - Register a new user
- `POST /auth/login` - Login and get access token

### Tasks
- `GET /tasks` - Get all tasks for the authenticated user
- `GET /tasks/{task_id}` - Get a specific task
- `POST /tasks` - Create a new task
- `PUT /tasks/{task_id}` - Update a task
- `DELETE /tasks/{task_id}` - Delete a task

## Usage Example

### 1. Register a user
```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"username": "john", "email": "john@example.com", "password": "securepass123"}'
```

### 2. Login
```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=john&password=securepass123"
```

### 3. Create a task (use the token from login)
```bash
curl -X POST "http://localhost:8000/tasks" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "description": "Milk, eggs, bread", "completed": false}'
```

### 4. Get all tasks
```bash
curl -X GET "http://localhost:8000/tasks" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

### 5. **Access your API**
   - Render will provide a URL like: `https://my-todo-api.onrender.com`
   - API docs at: `https://my-todo-api.onrender.com/docs`

### Database Configuration

- **Local Development**: Uses SQLite (no setup needed)
- **Production**: Uses PostgreSQL (set `DATABASE_URL` environment variable)

The app automatically detects and uses the appropriate database based on the `DATABASE_URL` environment variable.
