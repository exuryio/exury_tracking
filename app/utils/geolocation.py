import requests

def get_address(latitude: float, longitude: float):
    url = f"https://nominatim.openstreetmap.org/reverse"
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
        return data.get("address", {})
    return {}
