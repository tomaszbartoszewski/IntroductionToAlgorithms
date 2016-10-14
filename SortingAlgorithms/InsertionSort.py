def InsertionSort(arrayToSort):
    for i in range(1, len(arrayToSort)):
        key = arrayToSort[i]
        j = i - 1
        while (j >= 0 and arrayToSort[j] > key):
            arrayToSort[j+1] = arrayToSort[j]
            j = j-1
        arrayToSort[j+1] = key

array1 = [6,5,4,3,2,1]
InsertionSort(array1)
print(array1)
array2 = [1,2,3,4,5,5,6,7,8]
InsertionSort(array2)
print(array2)
array3 = [12,5,8,1,5,9,6,98,5,4,3]
InsertionSort(array3)
print(array3)
array4 = [1]
InsertionSort(array4)
print(array4)
array5 = []
InsertionSort(array5)
print(array5)