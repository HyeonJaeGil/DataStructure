#! /usr/bin/python

area = int(input('input number: '))

for _ in range(1, area+1):
    if _*_ > area: break
    if area % _ : continue
    print(f'{_} x {area // _}')
