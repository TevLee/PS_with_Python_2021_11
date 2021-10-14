import sys
#sys.stdin = open("in1.txt", "rt")

N, M = map(int, input().split())

pls = []

for n in range(1, N+1):
    for m in range(1, M+1):
        pls.append(n + m)

cnt = []

for i in range(1, N+M+1):
    c = 0
    for p in pls:
        if i == p:
            c += 1
    cnt.append(c)

max = max(cnt)

for i in range(len(cnt)):
    if cnt[i] == max:
        print(i+1, end=" ")
