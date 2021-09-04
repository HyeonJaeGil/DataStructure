#! /usr/bin/python


x = ['a', 'b', 'c']

for i in range(len(x)):
    print(f'x[{i}]={x[i]}')

for i, name in enumerate(x, 1):
    print(f'{i}th element = {name}')
 
for i in x:
     print(i)