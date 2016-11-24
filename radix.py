from random import randint

def radixSort (lista):
    digitos = len(str(max(lista)))
    mod = 10
    div = 1
    for digito in range(0, digitos):
        lista = ordenarRadix(mod, div, lista)
        mod *= 10
        div *= 10
    return lista

def ordenarRadix(mod, div, lista):
    auxiliar = [list() for x in range(0, 10)]
    resultado = []
    for num in lista:
        auxiliar[(num % mod) // div].append(num)
    for num in auxiliar:
        resultado.extend(num)
    return resultado
