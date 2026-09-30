import requests
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_arquivo(ano, semestre):
    if ano == 2022 and semestre == 1:
        extensao = 'zip'
        url = 'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/dsas/ca/precos-semestrais-ca.zip'

    elif ano >= 2022:
        extensao = 'zip'
        url = f'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/dsas/ca/ca-{ano}-{semestre:02d}.zip'

    else:
        extensao = 'csv'
        url = f'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/dsas/ca/ca-{ano}-{semestre:02d}.csv'

    logging.info(f'Tentando download do arquivo: ca-{ano}-{semestre:02d}.{extensao}')

    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            logging.info(f'Download em andamento: ca-{ano}-{semestre:02d}.{extensao}')
            os.makedirs('data/raw', exist_ok=True)
            with open(f'data/raw/ca-{ano}-{semestre:02d}.{extensao}.tmp', 'wb') as arquivo_final:
                for chunk in response.iter_content(chunk_size=8192):
                    arquivo_final.write(chunk)
            os.rename(f'data/raw/ca-{ano}-{semestre:02d}.{extensao}.tmp', f'data/raw/ca-{ano}-{semestre:02d}.{extensao}')
            logging.info(f'Download completo: data/raw/ca-{ano}-{semestre:02d}.{extensao}')

        else:
            logging.error(f'Falha no download do arquivo: ca-{ano}-{semestre:02d}.{extensao}. Status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        logging.error(f'Erro ao tentar baixar o arquivo: ca-{ano}-{semestre:02d}.{extensao}. Erro: {e}')


def download_arquivos(ano_inicio, ano_fim):
    logging.info(f'Iniciando download de arquivos de {ano_inicio} a {ano_fim}')
    for ano in range(ano_inicio, ano_fim + 1):
        for semestre in range(1, 3):
            download_arquivo(ano, semestre)
    logging.info('Download de todos os arquivos concluído.')