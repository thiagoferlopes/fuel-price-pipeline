import requests

def download(ano, semestre):
    url = f'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/dsas/ca/ca-{ano}-{semestre}.csv'
    response = requests.get(url, stream=True)
    with open(f'data/raw/ca-{ano}-{semestre}.csv', 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
