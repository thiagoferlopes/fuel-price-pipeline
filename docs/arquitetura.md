## Extract.py

1. __Padrão de URL__: O site da ANP expõe um link no formato: ``https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/dsas/ca/ca-{ano}-{semestre}.csv``. Vou precisar gerar essa URL para cada ano entre 2021-01 e 2026-01, substituindo {ano} e {semestre} no loop.

2. __Local de Salvamento__:Cada arquivo baixado vai para ``data/raw/ca_{ano}-{semestre}.csv``. O ano e o semestre no nome evita que um download sobrescreva o anterior sem eu perceber.

3. __Comportamento em 404__: Se um semestre não existir no servidor, o script registra no log qual ano e o seu semestre falhou e continua para o próximo, não parando a execução inteira. 
Justificativa: Se ocorreu algum problema na execução do script para download dos arquivos, não quero que o programa falhe totalmente, guardando o ano e o semestre desse arquivo nos logs, para verificação manual ao final do script.

4. __Comportamento de Queda de conexão no meio do download__: Primeira vez que eu particulamente penso nisso. Minha ideia é: caso ocorra algum erro de conexão, o arquivo parcial não fique salvo no lugar de um arquivo completo. Irei pesquisar se dá para validar isso de forma simples antes de aceitar como solução final.