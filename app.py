import imp
from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title = "REST API CRUD - Simple users management",
    description = "Simple users management REST API implement with fastAPI and sqlite relational database.",
    version = "1.0",
    openapi_tags=[{
        "name": "users",
        "description": "Users manipulation routes"
    }]
)

app.include_router(user)
