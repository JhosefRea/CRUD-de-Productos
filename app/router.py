from fastapi import APIRouter
from app.controllers.producto_controller import router as producto_router

router = APIRouter()

router.include_router(producto_router, prefix="/productos", tags=["productos"])





