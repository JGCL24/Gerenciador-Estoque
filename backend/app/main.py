from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import select
from typing import List

from .database import create_db_and_tables, get_session
from .models import Product, ProductCreate, ProductUpdate, Movement, MovementCreate
from sqlmodel import select
from datetime import datetime

app = FastAPI(title="Gerenciador de Estoque API")

origins = ["http://localhost:5173", "http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    """Create DB tables and print friendly App/Docs URLs to the console after startup.

    Uvicorn logs show "http://0.0.0.0:8000" which is correct for binding, but users
    often prefer to see the local URLs, so we print them using HOST/PORT env vars
    (defaults: 0.0.0.0:8000 -> shown as localhost:8000).
    """
    import os

    create_db_and_tables()

    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    display_host = host if host != "0.0.0.0" else "localhost"
    app_url = f"http://{display_host}:{port}"
    docs_url = f"{app_url}/docs"

    # Print after startup so messages appear after Uvicorn's logs
    print("")
    print("App:", app_url)
    print("Docs:", docs_url)
    print("")

@app.get("/products", response_model=List[Product])
def list_products(*, session=Depends(get_session)):
    products = session.exec(select(Product)).all()
    return products


@app.get("/movements")
def list_movements(*, session=Depends(get_session)):
    # return recent movements (sorted desc by timestamp)
    movements = session.exec(select(Movement).order_by(Movement.timestamp.desc())).all()
    return movements


@app.post("/movements", response_model=Movement, status_code=201)
def create_movement(*, movement: MovementCreate, session=Depends(get_session)):
    # validate product exists
    product = session.get(Product, movement.product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if movement.quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be greater than zero")

    # apply movement
    if movement.type not in ("entrada", "saida"):
        raise HTTPException(status_code=400, detail="Type must be 'entrada' or 'saida'")

    if movement.type == 'entrada':
        product.quantity = product.quantity + movement.quantity
    else:
        # saída: ensure we don't go negative
        if product.quantity - movement.quantity < 0:
            raise HTTPException(status_code=400, detail="Cannot remove more than current quantity")
        product.quantity = product.quantity - movement.quantity

    db_movement = Movement(product_id=movement.product_id, type=movement.type, quantity=movement.quantity, note=movement.note, timestamp=datetime.utcnow())
    session.add(db_movement)
    session.add(product)
    session.commit()
    session.refresh(db_movement)
    session.refresh(product)

    return db_movement
@app.post("/products", response_model=Product, status_code=201)
def create_product(*, product: ProductCreate, session=Depends(get_session)):
    db_product = Product.from_orm(product)
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product

@app.get("/products/{product_id}", response_model=Product)
def get_product(*, product_id: int, session=Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.put("/products/{product_id}", response_model=Product)
def update_product(*, product_id: int, product: ProductUpdate, session=Depends(get_session)):
    db_product = session.get(Product, product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    product_data = product.dict(exclude_unset=True)
    for key, value in product_data.items():
        setattr(db_product, key, value)
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product

@app.delete("/products/{product_id}", status_code=204)
def delete_product(*, product_id: int, session=Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    session.delete(product)
    session.commit()
    return None
