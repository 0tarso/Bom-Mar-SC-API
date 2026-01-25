from services.pdf_parser import parse_balneabilidade
from services.agrupar_por_cidade import agrupar_por_cidade
from services.salvar_relatorio import salvar_novo_relatorio
from services.buscar_ultimo_relatorio import buscar_ultimo_relatorio

from fastapi import HTTPException


def atualizar_relatorio():
    CAMINHO_RELATORIO_ATUALIZADO = buscar_ultimo_relatorio()

    if CAMINHO_RELATORIO_ATUALIZADO:
        print("Último arquivo encontrado:", CAMINHO_RELATORIO_ATUALIZADO)
    else:
        print("Nenhum arquivo de relatório encontrado.")

        raise HTTPException(status_code=404, detail="Sem relatorios")

    coletas = parse_balneabilidade(CAMINHO_RELATORIO_ATUALIZADO)

    resultado = agrupar_por_cidade(coletas)
    salvar_novo_relatorio(resultado)

    response = {
        "message": "relatórios atualizados com sucesso",
        "total_cidades": resultado.__len__(),
        "dados": dict(list(resultado.items())[:3]),
    }

    return response
