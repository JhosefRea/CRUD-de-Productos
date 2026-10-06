from pydantic import BaseModel, Field, EmailStr, ConfigDict, BeforeValidator
from app.dtos.detail_get_dto import DetailGetDTO
from app.models.producto_model import Address
from datetime import datetime
from typing import List, Optional, Annotated


PyObjectId = Annotated[str, BeforeValidator(str)]

class productoGetDTO(BaseModel):
    mongo_id: Optional[PyObjectId] = Field(alias="_id", default=None)
    id: str = Field(..., min_length=1, max_length=20, example="EC9160")
    createdAt: datetime = Field(default_factory=datetime.now, example="2025-01-22T00:00:00.000Z")
    name: datetime = Field(..., example="")
    price: float = Field(..., gt=0)
    stock: float = Field(..., gt=0)
    
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )

