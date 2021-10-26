#! /usr/bin/python

# Functions to implement
# __len__, is_empty, is_full, push, pop, 
# peek, clear, find, count, __contains__, dump
# Expection handling (Empty, Full) 

from typing import Any
from collections import deque

class Stack:
    def __init__(self, maxlen: int=256) -> None:
        self.capacity = maxlen
        self.__stk = deque([], maxlen)

    def __len__(self)->int:
        return len(self.__stk)
    
    def is_empty(self)->bool:
        return len(self.__stk) <= 0
    
    def is_full(self)->bool:
        return len(self.__stk) >= self.capacity
    
    def push(self, value: Any)->None:
        self.__stk.append(value)
    
    def pop(self)->Any:
        return self.__stk.pop()
    
    def peek(self)->None:
        return self.__stk[-1]


    def clear(self)->None:
        self.__stk.clear()
    
    
    def find(self, value:Any)->Any:
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1 

    def count(self, value:Any)->int:
        return self.__stk.count(value)
    

    def __contains__(self, value)->bool:
        return self.count(value)
    
    def dump(self)->None:
        print(list(self.__stk))
    