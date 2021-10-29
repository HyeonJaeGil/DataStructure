#! /usr/bin/python

from typing import MutableSequence


def selection_sort(a:MutableSequence) -> None:
    n = len(a)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
    

if __name__=="__main__":
    array = [4,3,6,5,7,9,0,3,2,1]
    print(f"input array: {array}")

    selection_sort(array)
    print(f"output array: {array}") # [0, 1, 2, 3, 3, 4, 5, 6, 7, 9] 