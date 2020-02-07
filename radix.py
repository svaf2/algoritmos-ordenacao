from random import randint

def radixSort (array):
    digits = len(str(max(array)))
    mod = 10
    div = 1
    for _ in range(0, digits):
        array = sortOnce(mod, div, array)
        mod *= 10
        div *= 10
    return array

def sortOnce(mod, div, array):
    aux = [list() for x in range(0, 10)]
    result = []
    for num in array:
        aux[(num % mod) // div].append(num)
    for num in aux:
        result.extend(num)
    return result
