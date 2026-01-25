from services.criar_mapa_praia_cidade import criar_mapa_praia_cidade
from services.normalizar_nome import normalizar_nome
import os
from collections import defaultdict
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# aponta para api_bom_mar_sc/

PRAIA_POR_CIDADE_CAMINHO = os.path.join(BASE_DIR, "data/praia_por_cidade.json")


def agrupar_por_cidade(coletas: list) -> dict:
    with open(PRAIA_POR_CIDADE_CAMINHO, "r", encoding="utf-8") as arquivo:
        praias_por_cidade = json.load(arquivo)

    mapa_praia_cidade = criar_mapa_praia_cidade(praias_por_cidade)
    resultado = defaultdict(list)

    for coleta in coletas:
        praia_normalizada = normalizar_nome(coleta["local"])
        cidade = mapa_praia_cidade.get(praia_normalizada, "Cidade não identificada")

        resultado[cidade].append(
            {
                "praia": praia_normalizada,
                "local": coleta["local"],
                "complemento": coleta["complemento"],
                "data_coleta": coleta["data_coleta"],
                "situacao": coleta["situacao"],
            }
        )

    return dict(resultado)
