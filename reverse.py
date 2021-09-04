#! /usr/bin/python

from typing import Any, MutableSequence


def reverse_array(a: MutableSequence) -> None:
    # return reversed array
    # note that arrays are mutable, but tuples are not.
    # so it can't reverse the tuple.
    n = len(a)
    for i in range(n//2):
        a[i], a[n-i-1] = a[n-i-1], a[i]


if __name__== '__main__':
    nx = int(input('the number of elements in array: '))
    x = [None] * nx
    for i in range(nx):
        x[i] = int(input(f'x[{i}] = '))
    print(f'original array: {x}')
    # x.reverse() # standard library
    # x = list(reversed(x)) # create new list with the iterator returned by reversed()
    # reverse_array(x)
    print(f'reversed array: {x}')
