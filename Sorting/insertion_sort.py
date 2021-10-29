#! /usr/bin/python

from typing import MutableSequence

def insertion_sort(a:MutableSequence) -> None:
    n = len(a)

    for i in range(n):
        temp = a[i]
        j = i
        while j > 0 and a[j-1] > temp:
            a[j] = a[j-1]
            j -= 1
        a[j] = temp


if __name__=="__main__":
    array = [4,3,6,5,7,9,0,8,2,1]
    print(f"input array: {array}")

    insertion_sort(array)
    print(f"output array: {array}") # [0, 1, 2, 3, 3, 4, 5, 6, 7, 9] 