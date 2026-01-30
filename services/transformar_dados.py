from collections import defaultdict


def tranformar_dados(dados_brutos: list) -> dict:
    dados_formatados = defaultdict(list)

    for item in dados_brutos:
        if not item.get("ANALISES"):
            continue

        ultima_analise = item["ANALISES"][0]

        municipio = item["MUNICIPIO"].title()

        situacao = "PRÓPRIA" if ultima_analise["CONDICAO"] == "PRÓPRIO" else "IMPRÓPRIA"

        dados_formatados[municipio].append(
            {
                "praia": item["BALNEARIO"],
                "local": f'{item["BALNEARIO"]} ({item["PONTO_NOME"]})',
                "complemento": item["LOCALIZACAO"],
                "data_coleta": ultima_analise["DATA"],
                "situacao": situacao,
                "latitude": item["LATITUDE"],
                "longitude": item["LONGITUDE"],
                "codigo_ibge": item["MUNICIPIO_COD_IBGE"],
            }
        )

    for municipio in dados_formatados:
        dados_formatados[municipio].sort(key=lambda x: x["praia"])

    dados_em_ordem_alfabetica = dict(
        sorted(dados_formatados.items(), key=lambda item: item[0])
    )

    return dados_em_ordem_alfabetica
