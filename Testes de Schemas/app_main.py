from fastapi import FastAPI
from app.routes.item_routes import router as item_router

app = FastAPI()
app.include_router(item_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
