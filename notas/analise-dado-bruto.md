Para analisar os dados propostos pela [ANP](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/serie-historica-de-precos-de-combustiveis) da categoria de combustíveis de automóveis, busquei identificar primeiramente se todos os cabeçalhos eram iguais e vi realmente que estava tudo padronizado, também analisei se ocorreu alguma alteração nos dados para identificar possíveis organizações e estratégias que iriam ser feitas para evitar valores inconsistentes (ex: parada nos registros feitos na coluna de Valor de Compra).

Com essa informação, busquei analisar a partir de qual semestre ocorreu essa alteração nos registros dos dados, visando garantir a construção de uma pipeline consistente, recortando a partir do semestre que os dados param de existir. Com isso, baixei os arquivos CSVs disponíveis por semestres de combustíveis automotivos do: 1° semestre de 2020, 2° semestre de 2020, 1° semestre de 2021 e 1° semestre de 2026.

Com os arquivos baixados, eu analisei primeiramente eles diretamente pelo editor de código do VS Code, porém tive problemas e acabei tendo pequenos deslizes por justamente analisar somente as primeiras linhas, acabando que, inicialmente, tirei conclusões erradas do ano em que parou de ser registrada a coluna com Valor de Compra. Ao perceber esse erro, optei por abrir o arquivo de maneira mais tradicional pelo próprio Excel, corrigindo esse erro de análise.

Com a análise feita utilizando os arquivos, consegui identificar que os semestres que estavam com os dados de Valor de Compra preenchidos eram:
- [x] 1° Semestre de 2020
- [x] 2° Semestre de 2020
- [ ] 1° Semestre de 2021
- [ ] 1° Semestre de 2026
