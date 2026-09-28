import requests
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download(ano, semestre):
    url = f'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/dsas/ca/ca-{ano}-{semestre}.csv'
    logging.info(f'Tentando download do arquivo: ca-{ano}-{semestre}.csv')

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        logging.info(f'Download em andamento: ca-{ano}-{semestre}.csv')
        os.makedirs('data/raw', exist_ok=True)
        with open(f'data/raw/ca-{ano}-{semestre}.csv', 'wb') as arquivo_final:
            for chunk in response.iter_content(chunk_size=8192):
                arquivo_final.write(chunk)
        logging.info(f'Download completo: data/raw/ca-{ano}-{semestre}.csv')
    else:
        logging.error(f'Falha no download do arquivo: ca-{ano}-{semestre}.csv. Status code: {response.status_code}')