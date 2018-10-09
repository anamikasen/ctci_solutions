array = [3, 2, 1, 6, 4, 19, 32, 0, -1]


def selectionsort(array):
    for i in range(0, len(array)-1):
        minindex = i
        for j in range(i+1, len(array)):
            if array[j] < array[minindex]:
                minindex = j
        if minindex!=i:
            array[i], array[minindex] = array[minindex], array[i]

    print(array)

if __name__=="__main__":
    selectionsort(array)
