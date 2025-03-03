from fastapi import FastAPI

app = FastAPI()

@app.get("/suma")
def sumar(a: int, b: int):
    """
    Recibe dos números enteros y devuelve la suma.
    Se accede a la API con: http://127.0.0.1:8000/suma?a=5&b=3
    """
    return {"resultado": a + b}
