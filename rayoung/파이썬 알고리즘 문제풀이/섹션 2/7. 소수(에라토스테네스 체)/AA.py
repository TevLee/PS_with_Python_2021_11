import sys
#sys.stdin = open("in1.txt", "rt")

N = int(input())
primes = [True] * (N+1)

cnt = 0

for i in range(2, N+1):
    if primes[i]:
        cnt += 1
        for j in range(i, N+1, i):
            primes[j] = False

print(cnt)
