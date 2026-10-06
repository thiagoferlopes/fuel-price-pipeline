# Modelagem

Fato(ca-{semeste}-{ano}): cada linha representa um item vendido de combustíveis automotivos, o que varia linha a linhe é Revenda, Data da Coleta, Valor de Venda, Valor de Compra. Colunas(FK): id_revendedor, id_endereco, id_combustivel.

Dimensão revendedor:CNPJ da Revenda e Bandeira. Repete em toda linha de vendas do mesmo revendedor, por isso vira tabela separada.

Dimensão combustivel: Produto. Repete em toda linha de venda do mesmo produto, por isso vira tabela separada.

Dimensão regiao: Região. Repete em toda linha que tem o mesmo estado, por isso vira tabela separada.

Dimensão estado: Estado. Repete em toda linha que tem o mesmo estado, por isso vira tabela separada.

Dimensão endereco: Nome da Rua, Numero da Rua, Complemento, Bairro, CEP e Município.Repete em toda linha que tem o mesmo local de revenda, por isso vira tabela separada. Colunas(FK): sigla_regiao, sigla_estado. 

Chaves: revendedor e combustivel não tem chave natural confiável no CSV de origem (nome pode repetir ou CPNJ, ter erro de digitação), vou gerar um ID artificial para cada um. Região e Estado eu derivo direto pela sigla, sem precisar de ID artificial complexo, posso usar a própria sigla como chave.

id_revendedor será gerado após normalização do CNPJ (remoção de formatação/pontuação), para evitar duplicar revendedor por incosistência de digitação do CNPJ de origem.

Endereço é referenciado direto pela fato, não pelo revendedor, porque um mesmo enderço físico pode ter CNPJs diferentes ao longo do tempo.