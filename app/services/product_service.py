from typing import List
from app.models.producto_model import producto
from app.dtos.product_post_dto import productoPostDTO
from app.dtos.product_get_dto import productoGetDTO
from app.database.database import mongodb
from bson import ObjectId

class productoService:
    def __init__(self):
        self.collection = mongodb.get_collection("productos")

    async def create_producto(self, producto: producto) -> productoPostDTO:
        producto_dict = self._prepare_producto_dict(producto)

        result = await self.collection.insert_one(producto_dict)

        producto_dict["_id"] = str(result.inserted_id)

        return productoPostDTO(**producto_dict)

    async def get_productos(self) -> List[productoGetDTO]:
        documents = await self.collection.find().to_list(100)
        return [self.document_to_producto(doc) for doc in documents]


    async def update_producto(self, number: str, update_data: dict) -> producto | None:
        result = await self.collection.update_one({"number": number}, {"$set": update_data})
        if result.modified_count:
            updated_producto = await self.get_producto_by_numero(number)
            return updated_producto
        return None


    async def delete_producto(self, number: str) -> bool:
        result = await self.collection.delete_one({"number": number})
        return result.deleted_count > 0


producto_service = productoService()
