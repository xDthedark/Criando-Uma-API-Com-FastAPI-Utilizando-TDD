from pydantic import ValidationError
from app.schemas.item import ItemSchema

def test_item_schema():
    item = ItemSchema(name="Laptop", description="A powerful laptop", price=1000.0, stock=10)
    assert item.name == "Laptop"
    assert item.price == 1000.0

def test_item_schema_invalid():
    try:
        ItemSchema(name="Laptop", description="A powerful laptop", price="invalid", stock=10)
    except ValidationError:
        assert True
