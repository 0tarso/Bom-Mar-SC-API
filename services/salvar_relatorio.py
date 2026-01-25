import datetime
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA_DATA = os.path.join(BASE_DIR, "data")
CAMINHO_ARQUIVO = os.path.join(PASTA_DATA, "relatorio_atualizado.json")


def salvar_novo_relatorio(dados):

    os.makedirs(PASTA_DATA, exist_ok=True)

    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    print(f"Arquivo salvo em: {CAMINHO_ARQUIVO}")
