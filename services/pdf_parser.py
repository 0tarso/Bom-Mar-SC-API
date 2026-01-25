import pdfplumber


def parse_balneabilidade(pdf_path: str):
    resultados = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()

            for table in tables:
                headers = table[0]

                # Garante que é a tabela correta
                if not headers or "SITUAÇÃO" not in headers:
                    continue

                for row in table[1:]:
                    if len(row) != 3:
                        continue

                    local_raw, data, situacao = row

                    if not local_raw:
                        continue

                    partes = local_raw.split("\n", 1)

                    resultados.append(
                        {
                            "local": partes[0].strip(),
                            "complemento": (
                                partes[1].strip() if len(partes) > 1 else None
                            ),
                            "data_coleta": data.strip() if data else None,
                            "situacao": situacao.strip() if situacao else None,
                        }
                    )

    return resultados
