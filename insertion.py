def insertionSort(lista):
    for x in range(1, len(lista)):
        index = x - 1
        while lista[index] > lista[index+1] and index >=0:
            lista[index], lista[index+1] = lista[index+1], lista[index]
            index -= 1
