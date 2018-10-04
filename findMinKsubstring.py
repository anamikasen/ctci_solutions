#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    i = 1
    currMin = arr[0] - arr[k]
    while(i<len(arr)-k):
        thisMin = arr[i]) - arr[i+k]
        if thisMin < currMin:
            currMin=thisMin
        i+=1

    return currMin

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
