from app.services.item_service import ItemService
from app.schemas.item import ItemSchema
from app.services.database import Database
from bson.objectid import ObjectId

def test_create_item():
    db = Database("mongodb://localhost:27017", "store_db")
    service = ItemService(db)
    item = ItemSchema(name="Laptop", description="A powerful laptop", price=1000.0, stock=10)
    item_id = service.create_item(item)
    assert ObjectId.is_valid(item_id)

def test_get_item():
    db = Database("mongodb://localhost:27017", "store_db")
    service = ItemService(db)
    item = ItemSchema(name="Laptop", description="A powerful laptop", price=1000.0, stock=10)
    item_id = service.create_item(item)
    retrieved_item = service.get_item(item_id)
    assert retrieved_item["name"] == "Laptop"
