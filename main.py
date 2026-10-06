from fastapi import FastAPI
import uvicorn
from app.router import router as api_router
from config.config import PORT


def create_app() -> FastAPI:
    app = FastAPI(
        title="PRODUCTS REST API",
        swagger_ui_parameters={
            "defaultModelsExpandDepth": -1,
            "docExpansion": "none"
        }
    )
    app.include_router(api_router, prefix="/api")
    return app

app = create_app()

def main():
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=int(PORT), reload=True)

if __name__ == "__main__":
    main()

