from pydantic import BaseModel, Field, ConfigDict


class Detalle(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )
