import csv

#-------------------FUNÇÕES--------------------------
#BUSCA OS DADOS DE UM ARQUIVO CSV. PARÂMETRO: NOME DO ARQUIVO
def getData(filename):
    file = open(filename, "r", encoding="cp437")
    next(file)
    data = list(csv.reader(file, delimiter=","))
    file.close()
    return data

def showMenu(dictionary):
    for key, value in dictionary.items():
        print(key, "\t", value)

def rank_top100(year, month):
    top100 = []
    songs_added = []  # lista para armazenar as músicas já adicionadas
    for row in billboard:
        dates = row[0].split("-")
        if year in dates[0] and month in dates[1]:
            song_name = row[2]  # Nome da música
            if song_name not in songs_added:  # Verifica se a música já foi adicionada
                top100.append(row)
                songs_added.append(song_name)  # Adiciona o nome da música ao conjunto de músicas adicionadas
    # Ordena a lista top_10 com base no valor máximo da coluna 6 (weeks-on-board)
    return sorted(top100, key=lambda x: int(x[6]), reverse=True)


def top_10_musics(year, month):
    top_10 = rank_top100(year, month)
    for i, song in enumerate(top_10[:10], start=1):
        print(f"{i}º - {song[2]} - {song[3]}")
            
def EachMonth(year):
    for month in range(1, 13):
        top_song = rank_top100(year, month=str(month))[0] #pega a primeira linha do top 100, que seria o top1
        print(f"{month}. {top_song[2]} - {top_song[3]}")

def top_100_musics(year, month):
    top_100 = rank_top100(year, month)
    for i, song in enumerate(top_100[:100], start=1):
        print(f"{i}º - {song[2]} - {song[3]}")
        
def artist(name):
    artists = []
    artist_counter = 0
    for i in billboard:
        if name.upper() in i[3].upper():
            print(f"{i[0]} - Rank: {i[1]} - Música: {i[2]}")
            artist_counter+=1
            print()
               
    if artist_counter == '1':
        print(f"Este artista foi citado {artist_counter} vez.")
    else:
        print(f"Este artista foi citado {artist_counter} vezes.")
    print()
    

def PositionSearch():
    year = input("Digite o ano solicitado (1955-2021): ")
    if year == '2021':
        month = input("Digite o mês solicitado (1-11): ")
    else:
        month = input("Digite o mês solicitado (1-12): ")
    position = int(input("Digite o número da posição que você deseja (1-100): "))
    top_100 = rank_top100(year, month)
    for i, song in enumerate(top_100[:100], start=1):
        if i == position:   
            print(f"\n{i}. {song[2]} - {song[3]}")
            
def top_music(year, month):
    top100artist = []
    artist_added = []  # Conjunto para armazenar os artistas já adicionados
    for row in billboard:
        dates = row[0].split("-")
        if year in dates[0] and month in dates[1]:
            artist_name = row[2]  # Nome da música
            if artist_name not in artist_added:  # Verifica se o artista já foi adicionado
               top100artist.append(row)
               artist_added.append(artist_name)  # Adiciona o nome do artista ao conjunto de artistas adicionados
        # Ordena a lista top_10 com base no valor máximo da coluna 6 (weeks-on-board)
    art = sorted(top100artist, key=lambda x: int(x[6]), reverse=True)
    for i, artist in enumerate(art[:1], start=1):
       print(f"O artista mais famoso do mês {month} foi {artist[3]} com {artist[6]} semanas seguidas no top 100.")

def famous_music():
    artist_counter  = {}
    for row in billboard:        
        artist = row[3]
        if artist in artist_counter:
            artist_counter[artist] += 1
        else:
            artist_counter[artist] = 1 
        
    max_artist = max(artist_counter, key=lambda x: artist_counter[x])
    times = artist_counter[max_artist]   
        
    print(f"Artista: {max_artist}")
    print(f"Quantidade de vezes que apareceu no top 100: {times}")

def executeMenu(option):
    print("\n\t\t\t", options[option], "\n")
    if option == "1":
        year = input("Digite o ano solicitado (1955-2021): ")
        if year == '2021':
            month = input("Digite o mês solicitado (1-11): ")
        else:
            month = input("Digite o mês solicitado (1-12): ")
        print()
        print("-"*65)
        print()
        top_10_musics(year, month)
        print()

    if option == "2":
        year = input("Digite o ano solicitado (1955-2021): ")
        print()
        print("-"*65)
        print()
        EachMonth(year)
        print()
        
    if option == "3":
        year = input("Digite o ano solicitado (1955-2021): ")
        if year == '2021':
            month = input("Digite o mês solicitado (1-11): ")
        else:
            month = input("Digite o mês solicitado (1-12): ")
        print()
        print("-"*65)
        print()
        top_100_musics(year, month)
        print()
        

    if option == "4":
        name = input("Digite o nome do artista solicitado: ")
        artist(name)

    if option == "5":
        print()
        PositionSearch()
        print()
        

    if option == "6":
        year = input("Digite o ano solicitado (1955-2021): ")
        if year == '2021':
            month = input("Digite o mês solicitado (1-11): ")
        else:
            month = input("Digite o mês solicitado (1-12): ")
        print()   
        top_music(year, month)
        print()
    if option == "7":        
        famous_music()
        print()
#----------------VARIÁVEIS---------------------------
billboard = getData("billboard.csv")
options = {"1":"Top 10 de um mês/ano específico",
           "2":"Top 12 do ano (1º de cada mês)",
           "3":"Top 100 de um mês/ano específico",
           "4":"Busca por artista",
           "5":"Busca por posição na lista no mês/ano",
           "6":"Artista que ficou mais semanas no mês/ano",
           "7":"Artista que mais apareceu na lista",
           "8":"Sair"}

#---------------PRINCIPAL----------------------------
selected = ""
while selected != "8":
    print("-"*65)
    print("Top 100 Músicas da Billboard (Janeiro de 1958 a Novembro de 2021")
    print("-"*65)
    showMenu(options)
    print("-"*65)
    selected = input("Selecione uma opção: ")
    print("-"*65)
    executeMenu(selected)
print("Obrigado por utilizar meus serviços!\nDesligando...")