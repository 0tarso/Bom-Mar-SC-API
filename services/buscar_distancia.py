import os
import httpx

OPEN_ROUTE_URL = "https://api.openrouteservice.org/v2/directions/driving-car"
API_KEY = os.getenv("OPEN_ROUTE_API_KEY")


async def buscar_distancia(
    de_long: float, de_lat: float, para_long: float, para_lat: float
):
    headers = {"Authorization": API_KEY, "Content-Type": "application/json"}

    payload = {
        "coordinates": [[de_long, de_lat], [para_long, para_lat]],
        "radiuses": [1500, 1500],
    }

    async with httpx.AsyncClient(timeout=10) as client:
        reposta_api_open_route = await client.post(
            OPEN_ROUTE_URL, json=payload, headers=headers
        )

        print(" =======  Print responsta da API =======")
        print("StatusCode -> ", reposta_api_open_route.status_code)

        reposta_api_open_route.raise_for_status()
        data = reposta_api_open_route.json()

        dados_distancia = data["routes"][0]["summary"]
        print("Response -> ", dados_distancia)

        return {
            "distancia_em_metros": dados_distancia["distance"],
            "distancia_em_km": round(dados_distancia["distance"] / 1000, 1),
            "duracao_estimada_minutos": round(dados_distancia["duration"] / 60),
        }
