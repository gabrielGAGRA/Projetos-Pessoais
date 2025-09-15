import os
import re
import requests
from bs4 import BeautifulSoup

# Directory where the files will be saved
save_directory = 'c:/Users/gabri/Documents/PROJETOS/PY/Codigos/AI/Hacka/LLM/Site'

# Ensure the directory exists
os.makedirs(save_directory, exist_ok=True)

# List of URLs to scrape
urls = [
    "https://www.pine.com/para-sua-empresa/credito/capital-de-giro/",
    "https://www.pine.com/para-sua-empresa/credito/nota-comercial/",
    "https://www.pine.com/para-sua-empresa/credito/conta-garantida/",
    "https://www.pine.com/para-sua-empresa/credito/fianca/",
    "https://www.pine.com/para-sua-empresa/credito/multisacado/",
    "https://www.pine.com/para-sua-empresa/credito/nce-cce/",
    "https://www.pine.com/para-sua-empresa/credito/cheque-empresa/",
    "https://www.pine.com/para-sua-empresa/credito/fgi-peac/",
    "https://www.pine.com/para-sua-empresa/credito/confirming/",
    "https://www.pine.com/para-sua-empresa/credito/cpr-financeira/",
    "https://www.pine.com/para-sua-empresa/investimentos/cdb/",
    "https://www.pine.com/para-sua-empresa/investimentos/compromissadas/",
    "https://www.pine.com/para-sua-empresa/investimentos/letra-financeira/",
    "https://www.pine.com/para-sua-empresa/cambio-e-trade-finance/carta-de-credito-de-importacao/",
    "https://www.pine.com/para-sua-empresa/cambio-e-trade-finance/cambio-pronto/",
    "https://www.pine.com/para-sua-empresa/cambio-e-trade-finance/cambio-futuro/",
    "https://www.pine.com/para-sua-empresa/cambio-e-trade-finance/finimp/",
    "https://www.pine.com/para-sua-empresa/derivativos/ndf/",
    "https://www.pine.com/para-sua-empresa/derivativos/opcoes/",
    "https://www.pine.com/para-sua-empresa/derivativos/swap/",
    "https://www.pine.com/para-sua-empresa/mercado-de-capitais/",
    "https://www.pine.com/para-sua-empresa/seguros/",
    "https://www.pine.com/para-sua-empresa/servicos/parcerias/",
    "https://www.pine.com/para-voce/investimentos/",
    "https://www.pine.com/para-voce/emprestimos/",
    "https://www.pine.com/para-voce/cartoes/",
    "https://www.pine.com/quem-somos/#historia-pine",
    "https://www.pine.com/quem-somos/#pilares-pine",
    "https://bancopine.gupy.io/",
    "https://www.pine.com/quem-somos/#onde-estamos",
    "https://www.pine.com/fale-conosco/",
    "https://www.pine.com/relacao-com-investidores/",
    "https://www.pine.com/relacao-com-investidores/governanca-corporativa/conselho-e-diretoria/",
    "https://www.pine.com/relacao-com-investidores/governanca-corporativa/estatutos-codigos-politicas/",
    "https://www.pine.com/relacao-com-investidores/governanca-corporativa/comites/",
    "https://www.pine.com/relacao-com-investidores/governanca-corporativa/estrutura-organizacional/",
    "https://www.pine.com/relacao-com-investidores/governanca-corporativa/composicao-acionaria/",
    "https://www.pine.com/relacao-com-investidores/gerenciamento-de-risco-e-capital/",       
    "https://www.pine.com/relacao-com-investidores/informacoes-publicas/central-de-resultados/",
    "https://www.pine.com/relacao-com-investidores/informacoes-publicas/documentos-entregues-a-cvm/",
    "https://www.pine.com/relacao-com-investidores/informacoes-publicas/dividendos/",        
    "https://www.pine.com/relacao-com-investidores/outras-informacoes/ratings/",
    "https://www.pine.com/relacao-com-investidores/documentos-regulatorios/atas-e-reunioes/",
    "https://www.pine.com/relacao-com-investidores/informacoes-publicas/apresentacoes-e-eventos/",
    "https://www.pine.com/relacao-com-investidores/informacoes-publicas/calendario-de-eventos/",
    "https://www.pine.com/m/alerta-ri/",
    "https://www.pine.com/fale-ri/",
    "https://www.pine.com/relacao-com-investidores/outras-informacoes/formularios-de-compliance/",
    "https://www.pine.com/relacao-com-investidores/outras-informacoes/prospectos/"
]

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Remove unwanted tags to avoid extracting text from buttons and navigation elements
    for tag in soup(['a', 'button', 'nav', 'header', 'footer', 'script', 'style']):
        tag.decompose()

    # Add periods after specific tags if not already present
    for tag in soup.find_all(['label', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'div']):
        if tag.string:
            text = tag.get_text(strip=True)
            if not text.endswith('.'):
                tag.string = text + '.'

    # Extract text from the remaining content
    text = soup.get_text(separator=' ')

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # Remove unusual line terminators
    text = re.sub(r'[\r\x0b\x0c\x1c-\x1f\u2028\u2029]', '', text)

    # Extract the last part of the URL, replace '-' with spaces, and remove trailing slashes
    last_part = url.rstrip('/').split('/')[-1]
    filename = last_part.replace('-', ' ') + '.txt'

    # Full file path
    file_path = os.path.join(save_directory, filename)

    # Save the extracted text to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)
        f.write('\n')
        f.write(url)