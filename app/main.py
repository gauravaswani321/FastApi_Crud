from fastapi import FastAPI

from app.routers import auth, users

app = FastAPI(swagger_ui_parameters={"deepLinking": False})
app.include_router(users.router)
app.include_router(auth.router)


@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}
