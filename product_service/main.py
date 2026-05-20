from fastapi import FastAPI, HTTPException

STUDENT_N = 8

app = FastAPI(title="Product Service N8")

PRODUCTS = {
    801: {
        "id": 801,
        "name": "Laptop Lenovo",
        "price": 1200,
        "stock": 5
    },

    802: {
        "id": 802,
        "name": "Logitech Mouse",
        "price": 40,
        "stock": 10
    },

    803: {
        "id": 803,
        "name": "Keychron Keyboard",
        "price": 100,
        "stock": 0
    }
}


@app.get("/products")
def get_products():
    return {
        "student_id": STUDENT_N,
        "products": list(PRODUCTS.values())
    }


@app.get("/products/{product_id}")
def get_product(product_id: int):

    if product_id not in PRODUCTS:
        raise HTTPException(status_code=404, detail="Product not found")

    return {
        "student_id": STUDENT_N,
        "product": PRODUCTS[product_id]
    }
