from fastapi import FastAPI
import uvicorn  

app = FastAPI()

from fastapi import FastAPI, HTTPException
import uvicorn  

app = FastAPI()

@app.get("/calculate/discount")
def calculate_discount(price: float, discount_percentage: float):
    if discount_percentage < 0:
        raise HTTPException(status_code=400, detail="Invalid discount percentage")

    final_price = price - (price * (discount_percentage / 100))
    return {"final_price": final_price}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Discount Calculator API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)