from fastapi import FastAPI
import uvicorn  

app = FastAPI()

def add(a: int, b: int):
    return a + b

@app.get("/calculate/discount")
def calculate_discount(price: float, discount_percentage: float):

    if discount_percentage < 0:
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail="Discount percentage cannot be negative")

    final_price = price - (price * (discount_percentage / 100))
    return {"final_price": round(final_price, 2)}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Discount Calculator API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)