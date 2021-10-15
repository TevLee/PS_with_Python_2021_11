import sys
#sys.stdin = open("in1.txt", "rt")

N = int(input())
ls = list(map(int, input().split()))

def reverse(x):
    r = int(str(x)[::-1])
    return r

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

for l in ls:
    r = reverse(l)
    if isPrime(r):
        print(r, end=" ")
