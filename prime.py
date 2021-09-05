#! /usr/bin/python


counter = 0
ptr = 0
prime = [None] * 500

# 2 and 3 are prime numbers
prime[ptr] = 2
ptr += 1
prime[ptr] = 3
ptr += 1


# version 1
# for n in range(5, 1001, 2): #only the odd numbers
#     for i in range(1,ptr):
#         counter += 1
#         if n % prime[i] == 0:
#             break
#     else:
#         prime[ptr] = n
#         ptr += 1

# version 2
for n in range(5, 1001, 2):
    i = 1
    while prime[i]*prime[i] < n:
        counter += 2
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1
        counter += 1


# print
for i in range(ptr):
    print(prime[i])