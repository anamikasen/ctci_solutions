array = [3, 2, 1, 6, 4, 19, 32, 0, -1]

def insertionsort(array):
    for i in range(1, len(array)):
        j =i-1
        while array[j] > array[j+1] and j>=0:
            array[j], array[j+1] = array[j+1], array[j]
            j -=1

    return array


if __name__=="__main__":
    print(insertionsort(array))
