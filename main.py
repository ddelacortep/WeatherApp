from fastapi import FastAPI
import requests
import os

app = FastAPI()



@app.get("/")
def get_clima(ciudad: str = "Barcelona"):
    api_key = os.getenv('API_KEY', 'mi_api_key_por_defecto')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    response = requests.get(url).json()
    if response.get("cod") != 200:
        return {"error": "Ciudad no encontrada"}
    
    return {
        "ciudad": response["name"],
        "temperatura": response["main"]["temp"],
        "descripcion": response["weather"][0]["description"]
    }

