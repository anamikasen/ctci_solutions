array = [3, 2, 1, 6, 4, 19, 32, 0, -1]

def quickSort(array):
    return quickSort2(array, 0, len(array)-1)

def quickSort2(array, low, high):
    if low < high:
        p = partition(array, low, high)
        quickSort2(array, low, p-1)
        quickSort2(array, p+1, high)

    return array

def partition(array, low, high):
    pivotIndex = getPivot(array, low, high)
    pivotValue = array[pivotIndex]
    array[pivotIndex], array[low] = array[low], array[pivotIndex]
    border = low

    for i in range(low, high+1):
        if array[i] < pivotValue:
            border += 1
            array[i], array[border] = array[border], array[i]
    array[pivotIndex], array[border] = array[border], array[pivotIndex]

    return border


def getPivot(array, low, high):
    mid = (low + high)//2
    pivot = high
    if array[low] < array[mid]:
        if array[mid] < array[high]:
            pivot = mid
    else:
        if array[low] < array[high]:
            pivot = low

    return pivot

if __name__=="__main__":
    print(quickSort(array))
