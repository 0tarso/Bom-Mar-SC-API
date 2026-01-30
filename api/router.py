from fastapi import APIRouter
from api.deps import api_key_dep
import json
import os
from datetime import datetime

from services.atualizar_dados import buscar_dados_IMA
from services.salvar_relatorio import salvar_novo_relatorio

from services.transformar_dados import tranformar_dados


router = APIRouter(prefix="/v1", dependencies=[api_key_dep])


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ULTIMO_RELATORIO = os.path.join(BASE_DIR, "data", "relatorio_atualizado.json")


@router.get("/balneabilidade")
def balneabilidade():
    with open(ULTIMO_RELATORIO, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return {"total": len(dados), "dados": dados}


@router.get("/verificar-api")
def verificar_api():
    return {"status": "ok"}


@router.get("/atualizar-relatorio")
def atualizar_relatorio():
    dados_brutos = buscar_dados_IMA()
    dados_formatados = tranformar_dados(dados_brutos)

    salvar_novo_relatorio(dados_formatados)

    return {
        "atualizado_em": datetime.utcnow().isoformat(),
        "total_municípios": len(dados_formatados),
        "dados": dados_formatados,
    }
