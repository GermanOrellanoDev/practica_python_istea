
from typing import Any
import requests


def obtener_clima(ciudad: str) -> dict[str, Any]:
    """Obtiene los datos meteorológicos actuales de una ciudad."""
    url = f"https://wttr.in/{ciudad}"
    parametros = {"format": "j1"}

    respuesta = requests.get(url, params=parametros, timeout=10)
    respuesta.raise_for_status()

    # Forzamos el tipado aquí para que coincida con el retorno de la función
    datos: dict[str, Any] = respuesta.json()
    return datos
