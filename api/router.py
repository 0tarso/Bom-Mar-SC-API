from fastapi import APIRouter
from api.deps import api_key_dep
import json
import os

from services.atualizar_relatorio import atualizar_relatorio

router = APIRouter(prefix="/v1", dependencies=[api_key_dep])


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ULTIMO_RELATORIO = os.path.join(BASE_DIR, "data", "relatorio_atualizado.json")


@router.get("/balneabilidade")
def balneabilidade():
    with open(ULTIMO_RELATORIO, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return {"total": len(dados), "dados": dados}


@router.get("/health")
def health():
    return {"status": "ok"}


@router.get("/update")
def update():
    response = atualizar_relatorio()
    return response
