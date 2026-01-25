import unicodedata
import re


def normalizar_nome(texto: str) -> str:
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    texto = re.sub(r"\(.*?\)", "", texto)
    texto = re.sub(r"\s+", " ", texto)
    return texto.strip().upper()
