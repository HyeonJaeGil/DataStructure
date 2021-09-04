#! /usr/bin/python


def base_conv(x:int, r:int) -> str:

    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d = ''

    while x > 0:
        d += dchar[x%r]
        x //= r

    return d[::-1]



if __name__== '__main__':
    print(base_conv(24, 2))