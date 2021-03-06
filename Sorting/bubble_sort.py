#! /usr/bin/python

from typing import MutableSequence


def bubble_sort(a: MutableSequence)->None:
    print("using bubble_sort ...")
    n = len(a)
    for i in range(n):
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]


def bubble_sort_quick_break(a: MutableSequence)->None:
    print("using bubble_sort with quick break ...")
    n = len(a)
    for i in range(n):
        change_count = 0
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                change_count += 1
        if change_count == 0:
            break

def bubble_sort_narrow_search(a: MutableSequence)-> None:
    print("using bubble_sort with narrow search ...")
    n = len(a)
    left_bound = 0
    while left_bound < n-1:
        last = n-1
        for j in range(n-1, left_bound, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        left_bound = last

def shacker_sort(a: MutableSequence)-> None:
    print("using shacker_sort ...")
    n = len(a)
    left = 0
    right = n-1

    while left < right:
        left_bound = right
        for j in range(right, left, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                left_bound = j
        left = left_bound

        for i in range(left, right):
            right_bound = left
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                right_bound = i
        right = right_bound


if __name__=="__main__":
    array = [4,3,6,5,7,9,0,3,2,1]
    print(f"input array: {array}")

    while (True):
        print("which algorithm? \n\
            1:bubble_sort \n\
            2:bubble_sort_quick_break \n\
            3:bubble_sort_narrow_search \n\
            4:shacker_sort \n\
            Your input:\t", end="")
        choice = int(input())
        if choice in {1,2,3,4}:
            break
        else: print("Not valid number, Try again...")

    func_dict = {
        1: bubble_sort,
        2: bubble_sort_quick_break,
        3: bubble_sort_narrow_search,
        4: shacker_sort
    }

    func_dict[choice](array)
    print(f"output array: {array}") # [0, 1, 2, 3, 3, 4, 5, 6, 7, 9]
            

