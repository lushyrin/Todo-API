from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from database import init_db
from routes_auth import router as auth_router
from routes_tasks import router as tasks_router

app = FastAPI(
    title="Todo API - Task Management System",
    description="""
    A RESTful API for managing tasks with JWT authentication.
    
    ## Features
    
    * **Authentication**: Register and login with JWT tokens
    * **Task Management**: Full CRUD operations for tasks
    * **Security**: JWT-based authentication and user-specific task access
    * **Validation**: Automatic input validation with detailed error messages
    
    ## Usage
    
    1. Register a new user at `/auth/register`
    2. Login at `/auth/login` to get your access token
    3. Use the token to access protected endpoints (click 🔒 Authorize button)
    4. Manage your tasks with the `/tasks` endpoints
    """,
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@example.com",
    },
    license_info={
        "name": "MIT",
    },
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        field = " -> ".join(str(loc) for loc in error["loc"])
        message = error["msg"]
        errors.append({"field": field, "message": message, "type": error["type"]})

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "detail": "Validation error",
            "errors": errors,
        },
    )


@app.exception_handler(ValidationError)
async def pydantic_validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "detail": "Validation error",
            "errors": exc.errors(),
        },
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "detail": "Internal server error",
            "message": str(exc),
        },
    )


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/", tags=["Root"])
def read_root():
    return {
        "message": "Welcome to Todo API - Task Management System",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc",
    }


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy"}


app.include_router(auth_router)
app.include_router(tasks_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
