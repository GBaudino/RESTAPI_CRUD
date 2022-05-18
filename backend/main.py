from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from apps.user.routes import user
from config import settings
import uvicorn

app = FastAPI(
    title = "REST API CRUD - Simple users management",
    description = "Simple users management REST API implement with fastAPI and sqlite relational database.",
    version = "1.0",
    openapi_tags=[{
        "name": "users",
        "description": "Users manipulation routes"
    }]
)

@app.get('/')
def redirect_to_docs():
    return RedirectResponse(url="/docs/")

@app.on_event("startup")
async def configure_routes():
    app.include_router(user)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )