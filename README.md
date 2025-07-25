# Currency Converter Function

A simple currency conversion API built with FastAPI and deployed on Render.  
It uses the [Frankfurter.app](https://www.frankfurter.app/) public API to convert from one currency to another.

This function is designed to be contributed to [func.live](https://www.func.live), a marketplace for cloud functions.

---

## 🚀 Features

- Live exchange rates from Frankfurter API.
- Accepts `from`, `to`, and `amount` as input.
- Returns converted amount with metadata.
- FastAPI backend, deployed on Render.

---

## 🛠️ API Endpoints

### 🔁 `POST /currency_converter`

Convert an amount from one currency to another.

#### Request Body:
```json
{
  "input": {
    "from": "USD",
    "to": "EUR",
    "amount": 100
  }
}
```

#### Response:
```json
{
  "output": {
    "amount": 100,
    "base": "USD",
    "date": "2025-07-23",
    "rates": {
      "EUR": 92.52
    }
  }
}
```

---

### 📄 `GET /currency_converter`

Returns documentation metadata required by func.live:

```json
{
  "name": "currency_converter",
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
```

---

## ⚙️ Local Development

1. Clone the repo  
2. Create a virtual environment  
3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the server:

```bash
uvicorn main:app --reload
```

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for interactive API testing.

---

## 🌐 Deployed Version

This function is deployed at:  
👉 [https://currency-converter-ojox.onrender.com/currency_converter](https://currency-converter-ojox.onrender.com/currency_converter)

---

## 📬 Contributing to func.live

1. Make sure your GET and POST routes are implemented correctly.
2. Deploy your app publicly (e.g. Render, Vercel).
3. Submit via `curl` with your bearer token.

---

## 📄 License

MIT License.
