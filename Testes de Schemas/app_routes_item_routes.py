#Adicione modelos se necessário e refatore o código para melhorar a estrutura.

#Crie controladores e rotas no FastAPI e escreva testes para eles.


from fastapi import APIRouter, HTTPException
from app.schemas.item import ItemSchema
from app.services.item_service import ItemService
from app.services.database import Database

router = APIRouter()
db = Database("mongodb://localhost:27017", "store_db")
service = ItemService(db)

@router.post("/items/", response_model=str)
def create_item(item: ItemSchema):
    return service.create_item(item)

@router.get("/items/{item_id}", response_model=ItemSchema)
def get_item(item_id: str):
    item = service.get_item(item_id)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

@router.put("/items/{item_id}", response_model=int)
def update_item(item_id: str, item: ItemSchema):
    return service.update_item(item_id, item)

@router.delete("/items/{item_id}", response_model=int)
def delete_item(item_id: str):
    return service.delete_item(item_id)

