from app.services.database import Database

def test_database_connection():
    db = Database("mongodb://localhost:27017", "store_db")
    collection = db.get_collection("items")
    assert collection.name == "items"
