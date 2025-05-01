import requests

def get_address(latitude: float, longitude: float) -> str:
    url = "https://nominatim.openstreetmap.org/reverse"
    params = {
        "format": "json",
        "lat": latitude,
        "lon": longitude
    }
    headers = {
        "User-Agent": "web-tracking-app"
    }

    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get("display_name", "Dirección no encontrada")
    return "Dirección no encontrada"

