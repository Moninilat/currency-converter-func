from fastapi import FastAPI, Request
from pydantic import BaseModel
import httpx

app = FastAPI()

@app.post("/currency-converter")
async def currency_converter(req: Request):
    body = await req.json()
    input_data = body.get("input")

    if not input_data:
        return {"output": "Missing 'input' field"}

    try:
        from_currency = input_data["from"]
        to_currency = input_data["to"]
        amount = input_data["amount"]

        url = f"https://api.frankfurter.app/latest?from={from_currency}&to={to_currency}&amount={amount}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            return {"output": data}
    except Exception as e:
        return {"output": f"Error: {str(e)}"}

@app.get("/currency-converter")
def docs():
    return {
        "name": "currency-converter",
        "description": "Converts an amount from one currency to another using the public Frankfurter API.",
        "input": {
            "type": "object",
            "description": "An object with 'from', 'to' and 'amount' fields.",
            "example": {
                "from": "USD",
                "to": "EUR",
                "amount": 100
            }
        },
        "output": {
            "type": "object",
            "description": "The converted amount with metadata from the Frankfurter API.",
            "example": {
                "amount": 100,
                "base": "USD",
                "date": "2025-07-23",
                "rates": {
                    "EUR": 92.52
                }
            }
        }
    }
