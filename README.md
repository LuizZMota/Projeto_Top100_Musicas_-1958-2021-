# Projeto_Top100_Musicas_1958-2021
Este foi meu projeto da faculdade no 1º semestre, com o objetivo de desenvolver um programa em Python que analise os dados de artistas que estiveram entre os mais populares nos últimos anos.
O arquivo "billboard.csv" apresenta os dados dos top 100 artistas na billboard por mês, desde janeiro de 1958 até novembro de 2021. Neste arquivo tem dados como date; rank; song; artist; last week; peak rank; weeks-on-board.
Criei um programa em python que me permite ler os dados deste arquivo e realizar as seguintes buscas / filtros:

1. Top 10 de um mês / ano específico
Perguntar ao usuário qual o ano e o mês desejados e retornar os 10 primeiros artistas no ranking

2. Top 12 do ano (1º de cada mês)
Perguntar ao usuário qual o ano desejado e retornar o primeiro do ranking de cada mês deste ano.

3. Top 100 de um mês / ano específico
Perguntar ao usuário qual o ano e o mês desejados e retornar os 100 artistas no ranking

4. Busca por artista
Perguntar ao usuário o nome do artista desejado e retornar todas as instâncias encontradas. No fim apresentar a informação de quantas vezes este artista apareceu na busca

5. Busca por posição na lista no mês / ano
Perguntar ao usuário qual o ano, o mês e a posição que deseja consultar e retornar os dados da música / artista para esta posição.

6. Artista que fico mais semanas no mês / ano
Perguntar ao usuário qual o ano e o mês desejados e retornar o artista que ficou por mais semanas em alguma posição do Top 100. Dizer quantas semanas este artista esteve no ranking.

7. Artista que mais apareceu na lista
Apresentar o nome do artista que apareceu mais vezes em todo o dataset (1958 a 2021). Informar o nome e quantas vezes ele apareceu entre os Top 100

Os requisitos foram:

1. Leitura e análise do arquivo
O programa deve ser capaz de ler o arquivo de log e extrair as informações relevantes de cada linha. De forma a gerar os relatórios solicitados acima.

2. O programa deve apresentar um menu iterativo que permita ao usuário escolher a opção desejada em um loop contínuo até que ele opte por sair.
Sendo o menu construído usando um dicionário de opções e uma função que apresenta o dicionário criado. Este menu deve ser construído usando um dicionário de opções e uma função que apresenta o dicionário criado

3. Cada opção do menu deve ter sua própria função definida e chamada no loop principal.

4. Devem ser criadas funções auxiliares que possam ser reutilizadas nas demais funções, como por exemplo uma função que filtre uma lista de dados de acordo com o ano desejado. É importante definir quais funções precisam ser ciadas com base nos relatórios acima.
