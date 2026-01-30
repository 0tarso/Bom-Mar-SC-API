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
