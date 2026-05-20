from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

STUDENT_N = 8

app = FastAPI(title="Order Service N8")

PRODUCT_SERVICE_URL = "http://product-service-08:8000"

ORDERS = []


class OrderRequest(BaseModel):
    product_id: int
    quantity: int


@app.post("/orders")
def create_order(order: OrderRequest):

    try:
        response = requests.get(
            f"{PRODUCT_SERVICE_URL}/products/{order.product_id}"
        )

    except requests.exceptions.ConnectionError:
        raise HTTPException(
            status_code=503,
            detail="Product Service unavailable"
        )

    if response.status_code == 404:
        raise HTTPException(
            status_code=400,
            detail="Product does not exist"
        )

    product_data = response.json()["product"]

    if product_data["stock"] < order.quantity:
        raise HTTPException(
            status_code=400,
            detail="Not enough stock"
        )

    new_order = {
        "student_id": STUDENT_N,
        "order_id": len(ORDERS) + 1,
        "product_id": order.product_id,
        "product_name": product_data["name"],
        "quantity": order.quantity,
        "total_price": product_data["price"] * order.quantity,
        "status": "Created"
    }

    ORDERS.append(new_order)

    return new_order


@app.get("/orders")
def get_orders():

    return {
        "student_id": STUDENT_N,
        "orders": ORDERS
    }
