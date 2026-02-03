from fastapi import FastAPI
import requests
import os

app = FastAPI()



@app.get("/")

def home():
    return {
        "proyecto": "Weather App API - DevOps Portfolio",
        "autor": "ddelacortep",
        "estado": "Online",
        "endpoints_disponibles": {
            "clima": "/clima?ciudad={nombre_ciudad}",
            "documentacion": "/docs"
        }
    }

@app.get("/clima")
def get_clima(ciudad: str = "Barcelona"):
    api_key = os.getenv('API_KEY', 'mi_api_key_por_defecto')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    response = requests.get(url).json()
    if response.get("cod") != 200:
        return {"error": "Ciudad no encontrada"}
    
    return {
        "ciudad": response["name"],
        "pais": response["sys"]["country"],
        "temperatura": f"{response['main']['temp']}°C",
        "sensacion_termica": f"{response['main']['feels_like']}°C",
        "humedad": f"{response['main']['humidity']}%",
        "descripcion": response["weather"][0]["description"],
        "viento": f"{response['wind']['speed']} m/s"
    }

