listaVotacao = {1: 'Boto-Cor-De-Rosa', 2: 'Mico-Leão-Dourado',
                3: 'Arara-azul', 4: 'Onça-pintada', 5: 'Sucuri',
                6: 'Capivara', 7: 'Ariranha'}

num_votes = [1, 2, 3, 4, 5, 6, 7, 7, 2, 3, 1, 4, 2, 3, 4]

ranking = {}

def List():
    lista_max= max(listaVotacao)
    lista_min= min(listaVotacao)
    print('\nLISTA PARA VOTAR:')
    for numero in range (lista_min, lista_max+1):
        print(numero, ':', listaVotacao[numero])
        
def Vote():
    lista_max= max(listaVotacao)
    lista_min= min(listaVotacao)

    List()
    vote = int(input('Digite o número do seu voto: '))
    if (lista_min < vote < lista_max):
        num_votes.append(vote)
        Rank(num_votes)
        print("Voto computado!") 
    else:
        print("Seu voto foi nulo!")    

def Rank(lista):
    contador = 0
    tranporte = {}
    lista_max= max(lista)
    lista_min= min(lista)

    for numero in range (lista_min, lista_max+1):
        for item in lista:
            if item == numero:
                contador += 1
              
        tranporte.update({numero:contador})
        contador = 0  
    ranking.update(tranporte)

def Ranked():
    Rank(num_votes)
    lista_max= max(ranking)
    lista_min= min(ranking)
    print('\nRANKING:')
    for numero in range (lista_min, lista_max+1):
        print(numero, '=', listaVotacao[numero],'|', ranking[numero], 'vts')