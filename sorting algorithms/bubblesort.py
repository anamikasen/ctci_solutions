array = [3, 2, 1, 6, 4, 19, 32, 0]

def bubbleSort(array):

    for i in range(0, len(array)-1):
        for j in range(0, len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    print(array)


if __name__=="__main__":
    bubbleSort(array)
