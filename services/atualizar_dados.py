import requests
import json
from datetime import datetime
from pathlib import Path

IMA_URL = "https://balneabilidade.ima.sc.gov.br/relatorio/mapa"

DATA_PATH = Path("/data")
CACHE_FILE = DATA_PATH / "balneabilidade.json"


def buscar_dados_IMA():
    response = requests.get(IMA_URL, timeout=30)
    response.raise_for_status()
    return response.json()


def normalizar_dados(dados_brutos: list):
    dados_normalizados = []

    for item in dados_brutos:
        if not item.get("ANALISES"):
            continue

        ultima_analise = item["ANALISES"][0]

        dados_normalizados.append(
            {
                "id": item["CODIGO"],
                "municipio": item["MUNICIPIO"],
                "municipio_ibge": item["MUNICIPIO_COD_IBGE"],
                "balneario": item["BALNEARIO"],
                "ponto_nome": item["PONTO_NOME"],
                "localizacao": item["LOCALIZACAO"],
                "latitude": float(item["LATITUDE"]),
                "longitude": float(item["LONGITUDE"]),
                "status": ultima_analise["CONDICAO"],
                "data": ultima_analise["DATA"],
                "chuva": ultima_analise["CHUVA"],
                "e_coli": int(ultima_analise["RESULTADO"]),
                "temp_agua": int(ultima_analise["TEMP_AGUA"]),
            }
        )

    return {
        "updated_at": datetime.utcnow().isoformat(),
        "total": len(dados_normalizados),
        "data": dados_normalizados,
    }


def save_cache(data: dict):
    DATA_PATH.mkdir(parents=True, exist_ok=True)

    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def update_cache():
    raw = buscar_dados_IMA()
    normalized = normalizar_dados(raw)
    save_cache(normalized)

    return normalized
