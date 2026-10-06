from fastapi import APIRouter, HTTPException, status
from pydantic import ValidationError
from fastapi.encoders import jsonable_encoder
from typing import List
from app.dtos.producto_post_dto import productoPostDTO
from app.dtos.producto_get_dto import productoGetDTO
from app.services.producto_service import producto_service

router = APIRouter()

@router.post("/productos", response_model=productoPostDTO)
async def create_producto(producto_dto: productoPostDTO):
    try:
        # Convertir DTO a dict con alias y crear el modelo producto
        producto = producto(**producto_dto.model_dump(by_alias=True))

        # Llamar al servicio para guardar en MongoDB
        return await producto_service.create_producto(producto)
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=jsonable_encoder(e.errors()),
        )

@router.get("/productos", response_model=List[productoGetDTO])
async def get_productos():
    productos = await producto_service.get_productos()
    if not productos:
        raise HTTPException(status_code=404, detail="No productos found")
    return [productoGetDTO(**producto.model_dump(by_alias=True)) for producto in productos]



@router.get("/productos/{id}", response_model=productoGetDTO)
async def get_producto(id: str):
    producto = await producto_service.get_producto_by_id(id)
    if not producto:
        raise HTTPException(status_code=404, detail="producto not found")
    return producto


@router.put("/productos/{number}", response_model=productoPostDTO)
async def update_producto(number: str, producto_dto: productoPostDTO):
    updated_producto = await producto_service.update_producto(number, producto_dto.model_dump(exclude_unset=True))
    if not updated_producto:
        raise HTTPException(status_code=404, detail="producto not found")
    return productoPostDTO(**updated_producto.model_dump())


@router.delete("/productos/{number}", response_model=bool)
async def delete_producto(number: str):
    return await producto_service.delete_producto(number)
