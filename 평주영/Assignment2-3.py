# Assignment 2-3
n = int(input())

for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end='')

    for j in range(2*i-1):
        print("*", end='')
    print("")

for i in range(2, n+1):
    for j in range(i-1):
        print(" ", end='')

    for j in range(2*n-i*2+1):
        print("*", end='')
    print("")