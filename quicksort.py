def quicksort(array):
    return qs(0, len(array) - 1, array)

def qs(left, right, array):
    if left < right:
        pivot = part(left, right, array)
        qs(left, pivot - 1, array)
        qs(pivot + 1, right, array)

def getPivot(left, right, array):
    middle = (left + right) // 2
    pivot = right
    if array[left] < array[middle]:
        if array[middle] < array[right]:
            pivot = middle
    elif array[left] < array[right]:
        pivot = left
    return pivot

def part(left, right, array):
    index = getPivot(left, right, array)
    pivot = array[index]
    array[index], array[left] = array[left], array[index]
    count = left
    for x in range(left, right + 1):
        if array[x] < pivot:
            count += 1
            array[x], array[count] = array[count], array[x]
    array[left], array[count] = array[count], array[left]
    return count
