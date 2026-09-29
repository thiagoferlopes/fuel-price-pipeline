import requests
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_arquivo(ano, semestre):
    url = f'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/dsas/ca/ca-{ano}-{semestre:02d}.zip'
    logging.info(f'Tentando download do arquivo: ca-{ano}-{semestre:02d}.zip')

    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            logging.info(f'Download em andamento: ca-{ano}-{semestre:02d}.zip')
            os.makedirs('data/raw', exist_ok=True)
            with open(f'data/raw/ca-{ano}-{semestre:02d}.zip', 'wb') as arquivo_final:
                for chunk in response.iter_content(chunk_size=8192):
                    arquivo_final.write(chunk)
            logging.info(f'Download completo: data/raw/ca-{ano}-{semestre:02d}.zip')
        else:
            logging.error(f'Falha no download do arquivo: ca-{ano}-{semestre:02d}.zip. Status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        logging.error(f'Erro ao tentar baixar o arquivo: ca-{ano}-{semestre:02d}.zip. Erro: {e}')

def download_arquivos(ano_inicio, ano_fim):
    logging.info(f'Iniciando download de arquivos de {ano_inicio} a {ano_fim}')
    for ano in range(ano_inicio, ano_fim + 1):
        for semestre in range(1, 3):
            download_arquivo(ano, semestre)
    logging.info('Download de todos os arquivos concluído.')