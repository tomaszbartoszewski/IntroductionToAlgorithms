def SelectionSort(arrayToSort):
    arrayLength = len(arrayToSort)
    for i in range(0, arrayLength-1):
        minimum = arrayToSort[i]
        indexToReplaceCurrent = i
        for j in range(i, arrayLength):
            if (arrayToSort[j] < minimum):
                minimum = arrayToSort[j]
                indexToReplaceCurrent = j
        temp = arrayToSort[i]
        arrayToSort[i] = minimum
        arrayToSort[indexToReplaceCurrent] = temp

array1 = [6,5,4,3,2,1]
SelectionSort(array1)
print(array1)
array2 = [1,2,3,4,5,5,6,7,8]
SelectionSort(array2)
print(array2)
array3 = [12,5,8,1,5,9,6,98,5,4,3]
SelectionSort(array3)
print(array3)
array4 = [1]
SelectionSort(array4)
print(array4)
array5 = []
SelectionSort(array5)
print(array5)