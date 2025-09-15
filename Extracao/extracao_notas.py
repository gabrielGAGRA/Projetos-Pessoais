from math import e
from os import error
import re


def calcular_media_notas(pdf_path):
    """
    Calcula a média das notas da coluna 'Nota' em um arquivo PDF.

    Args:
        pdf_path (str): O caminho para o arquivo PDF.

    Returns:
        float: A média das notas, ou None se não for possível calcular.
    """

    notas = []
    extrair_notas = False

    # Abre o arquivo PDF (simulando a leitura do texto)
    try:
        with open(pdf_path, "r", encoding="utf-8") as file:
            pdf_text = file.read()
    except error:
        with open(pdf_path, "r", encoding="latin-1") as file:
            pdf_text = file.read()

    linhas = pdf_text.split("\n")

    for linha in linhas:
        linha = linha.strip()

        if '"Nota"' in linha:
            extrair_notas = True
            continue

        if extrair_notas and linha:
            parts = re.split(r'","', linha)
            if len(parts) >= 3:
                nota_str = parts[2].replace('"', "").replace(",", ".")
                try:
                    nota = float(nota_str)
                    notas.append(nota)
                except ValueError:
                    continue  # Ignora linhas que não são números válidos

    if notas:
        return sum(notas) / len(notas)
    else:
        return None


# Substitua 'seu_arquivo.pdf' pelo caminho do seu arquivo PDF
pdf = r"C:\Users\gabri\Downloads\P1-2025.pdf"
media = calcular_media_notas(pdf)

if media is not None:
    print(f"A média das notas é: {media:.2f}")
