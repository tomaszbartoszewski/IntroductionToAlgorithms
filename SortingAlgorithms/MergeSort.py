import math

def Merge(array, startIndex, middlePointIndex, endIndex):
    n1 = middlePointIndex - startIndex + 1
    n2 = endIndex - middlePointIndex + 1
    leftArray = []
    rightArray = []
    
    for i in range(0, n1):
        leftArray.append(array[startIndex + i])
    for j in range(1, n2):
        rightArray.append(array[middlePointIndex + j])
    i = 0
    j = 0

    for k in range(startIndex, endIndex + 1):
        if (i >= len(leftArray) or (j < len(rightArray) and rightArray[j] < leftArray[i])):
            array[k] = rightArray[j]
            j = j + 1
        elif (j >= len(rightArray) or leftArray[i] <= rightArray[j]):        
            array[k] = leftArray[i]
            i = i + 1

def MergeSortImpl(array, startIndex, endIndex):
    if (startIndex < endIndex):
        middlePointIndex = math.floor((startIndex + endIndex) / 2)
        MergeSortImpl(array, startIndex, middlePointIndex)
        MergeSortImpl(array, middlePointIndex + 1, endIndex)
        Merge(array, startIndex, middlePointIndex, endIndex)
    array

def MergeSort(array):
    MergeSortImpl(array, 0, len(array)-1)

array1 = [6,5,4,3,2,1]
MergeSort(array1)
print(array1)
array2 = [1,2,3,4,5,5,6,7,8]
MergeSort(array2)
print(array2)
array3 = [12,5,8,1,5,9,6,98,5,4,3]
MergeSort(array3)
print(array3)