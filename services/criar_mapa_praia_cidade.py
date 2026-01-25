from services.normalizar_nome import normalizar_nome


def criar_mapa_praia_cidade(praias_por_cidade):
    mapa = {}

    for item in praias_por_cidade:
        chave = normalizar_nome(item["praia"])
        mapa[chave] = item["cidade"]

    return mapa
