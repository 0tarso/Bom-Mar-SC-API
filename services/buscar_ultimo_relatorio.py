import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# aponta para api_bom_mar_sc/

PASTA_RELATORIOS = os.path.join(BASE_DIR, "relatorios")


def buscar_ultimo_relatorio():
    arquivos = os.listdir(PASTA_RELATORIOS)

    padrao = re.compile(r"relatorio_n(\d+)-\d+\.pdf")

    arquivos_numerados = [
        (int(padrao.match(f).group(1)), f) for f in arquivos if padrao.match(f)
    ]

    if not arquivos_numerados:
        return None

    _, ultimo_arquivo = max(arquivos_numerados, key=lambda x: x[0])

    return os.path.join(PASTA_RELATORIOS, ultimo_arquivo)
