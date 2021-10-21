import sys
#sys.stdin = open("in1.txt", "rt")

N = int(input())
ls = []
for _ in range(N):
    l = list(map(int, input().split()))
    ls.append(l)

M = int(input())
for _ in range(M):
    w, d, t = map(int, input().split())
    if d == 0:
        for _ in range(t):
            ls[w-1].append(ls[w-1].pop(0))
    else:
        for _ in range(t):
            ls[w-1].insert(0, ls[w-1].pop())

s = 0
m = N // 2

for i in range(N):
    if i <= m:
        a = ls[i][i:N - i]
    else:
        a = ls[i][N - 1 - i:i + 1]
    s += sum(a)

print(s)
