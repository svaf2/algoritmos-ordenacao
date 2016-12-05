''' Importa funcoes necessarias para o desenvolvimento do projeto '''
import timeit
import sys
from random import randint
sys.setrecursionlimit(5000)

# Inicio do insertion sort
def insertion(lista):
    for x in range(1, len(lista)):
        index = x - 1
        while lista[index] > lista[index+1] and index >=0:
            lista[index], lista[index+1] = lista[index+1], lista[index]
            index -= 1
    return lista    
# Fim do insertion sort

# Inicio do radix sort
def radix (lista):
    digitos = len(str(max(lista)))
    mod = 10
    div = 1
    for digito in range(0, digitos):
        lista = ordenarRadix(mod, div, lista)
        mod *= 10
        div *= 10
    return lista

''' A funcao abaixo cria os buckets, ordena elementos pelo caractere passado como parametro
a partir de uma operacao de divisao e mod e retorna uma lista ordenada '''
def ordenarRadix(mod, div, lista):
    auxiliar = [list() for x in range(0, 10)]
    resultado = []
    for num in lista:
        auxiliar[(num % mod) // div].append(num)
    for num in auxiliar:
        resultado.extend(num)
    return resultado
# Fim do radix sort

# Inicio do quicksort
''' Chamada principal da funcao em que passamos apenas a lista como parametro '''
def quicksort(lista):
    qs(lista, 0, len(lista)-1)

''' Chamada auxiliar, aqui utilizamos a recursao para particionar o vetor em vetores menores '''
def qs(lista, esquerda, direita):
    if esquerda < direita:
        pivo = part(lista, esquerda, direita)
        qs(lista, esquerda, pivo - 1)
        qs(lista, pivo + 1, direita)

''' Funcao que ordena o vetor particionado passado como parametro, retorna a posicao do pivo que estara
em sua posicao correta ao final da execucao '''
def part(lista, esquerda, direita):
    index = (esquerda + direita) // 2
    lista[esquerda], lista[index] = lista[index], lista[esquerda]
    pivo = lista[esquerda]
    i = esquerda + 1
    j = direita

    while True:
        while lista[i] <= pivo:
            if i >= direita: break
            i += 1

        while lista[j] >= pivo:
            if j <= esquerda: break
            j -= 1
        if i >= j: break
        lista[i], lista[j] = lista[j], lista[i]
    lista[esquerda], lista[j] = lista[j], lista[esquerda]
    return j
# Fim do quicksort

''' Funcao auxiliar que retorna a media dos testes obtidos a partir do metodo timeit '''
def media(lista, soma = 0):
    for x in lista:
        soma += x
    soma = soma / 10
    return str(soma)

''' Abaixo uma lista de todos os vetores que foram testados em cada algoritmo (com algumas excecoes
que estao explicadas no relatorio) '''

# Vetores aleatorios
pinsertion = [randint(0, 10**4) for x in range(0, 10**3)]
pAQuarta = [randint(0, 10**4) for x in range(0, 10**4)]
pAQuinta = [randint(0, 10**5) for x in range(0, 10**5)]
pASexta = [randint(0, 10**6) for x in range(0, 10**6)]
ginsertion = [randint(10**12, 10**14) for x in range(0, 10**3)]
gAQuarta = [randint(10**12, 10**14) for x in range(0, 10**4)]
gAQuinta = [randint(10**12, 10**14) for x in range(0, 10**5)]
gASexta = [randint(10**12, 10**14) for x in range(0, 10**6)]
rinsertion = [randint(0, 10) for x in range(0, 10**3)]

# Vetores com repeticao
rAQuarta = [randint(0, 100) for x in range(0, 10**4)]
rAQuinta = [randint(0, 100) for x in range(0, 10**5)]
rASexta = [randint(0, 100) for x in range(0, 10**6)]

# Vetores ordenados crescentes
pOCinsertion = [x for x in range(0, 10**3)]
pOCQuarta = [x for x in range(0, 10**4)]
pOCQuinta = [x for x in range(0, 10**5)]
pOCSexta = [x for x in range(0, 10**6)]
gOCinsertion = [x for x in range(0, 10**3)]
gOCQuarta = [10**12 + x for x in range(0, 10**4)]
gOCQuinta = [10**12 + x for x in range(0, 10**5)]
gOCSexta = [10**12 + x for x in range(0, 10**6)]

# Vetores ordenados decrescentes
pODinsertion = [x for x in range(10**3, 0, -1)]
pODQuarta = [x for x in range(10**4, 0, -1)]
pODQuinta = [x for x in range(10**5, 0, -1)]
pODSexta = [x for x in range(10**6, 0, -1)]
gODinsertion = [10**12 + x for x in range(10**3, 0, -1)]
gODQuarta = [10**12 + x for x in range(10**4, 0, -1)]
gODQuinta = [10**12 + x for x in range(10**5, 0, -1)]
gODSexta = [10**12 + x for x in range(10**6, 0, -1)]

# Fim da lista de vetores

''' Exemplo do metodo utilizado para computar o tempo de execucao para cada algoritmo '''

exemploInsertion = timeit.repeat("insertion({0})".format(pinsertion), "from __main__ import insertion", repeat = 10, number = 1)
exemploQuicksort = timeit.repeat("quicksort({0})".format(ginsertion), "from __main__ import quicksort", repeat = 10, number = 1)
exemploRadix = timeit.repeat("radix({0})".format(rinsertion), "from __main__ import radix", repeat = 10, number = 1)

''' O timeit retorna uma lista com o tempo de execucao de cada teste realizado, ele realiza o numero de testes passado como
parametro em repeat, eu escrevi cada lista em um arquivo de texto e transferi as informacoes para o excel para plotar
os graficos '''
