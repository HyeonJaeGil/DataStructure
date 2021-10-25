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