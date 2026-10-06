from pydantic import BaseModel, Field, EmailStr
from app.models.detalle_model import Detalle
from app.models.producto_model import Address
from datetime import datetime
from typing import List

class productoPostDTO(BaseModel):
    id: str = Field(..., min_length=1, max_length=20, example="EC9160")
    createdAt: datetime = Field(default_factory=datetime.now, example="2025-01-22T00:00:00.000Z")
    name: datetime = Field(..., example="")
    price: float = Field(..., gt=0)
    stock: float = Field(..., gt=0)


    class Config:
        allow_population_by_field_name = True # Permite usar tanto alias como nombres originales en DTO
        arbitrary_types_allowed = True
