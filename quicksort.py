def quicksort(lista):
    return qs(0, len(lista) - 1, lista)

def qs(esquerda, direita, lista):
    if esquerda < direita:
        pivo = part(esquerda, direita, lista)
        qs(esquerda, pivo - 1, lista)
        qs(pivo + 1, direita, lista)

def retornarPivo(esquerda, direita, lista):
    meio = (esquerda + direita) // 2
    pivo = direita
    if lista[esquerda] < lista[meio]:
        if lista[meio] < lista[direita]:
            pivo = meio
    elif lista[esquerda] < lista[direita]:
        pivo = esquerda
    return pivo

def part(esquerda, direita, lista):
    index = retornarPivo(esquerda, direita, lista)
    pivo = lista[index]
    lista[index], lista[esquerda] = lista[esquerda], lista[index]
    contador = esquerda
    for x in range(esquerda, direita + 1):
        if lista[x] < pivo:
            contador += 1
            lista[x], lista[contador] = lista[contador], lista[x]
    lista[esquerda], lista[contador] = lista[contador], lista[esquerda]
    return contador

