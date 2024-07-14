from app.services.database import Database
from app.schemas.item import ItemSchema
from bson.objectid import ObjectId

class ItemService:
    def __init__(self, db: Database):
        self.db = db.get_collection("items")

    def create_item(self, item: ItemSchema):
        result = self.db.insert_one(item.dict())
        return str(result.inserted_id)

    def get_item(self, item_id: str):
        return self.db.find_one({"_id": ObjectId(item_id)})
