def insertionSort(array):
    for x in range(1, len(array)):
        index = x - 1
        while array[index] > array[index + 1] and index >= 0:
            array[index], array[index + 1] = array[index + 1], array[index]
            index -= 1
