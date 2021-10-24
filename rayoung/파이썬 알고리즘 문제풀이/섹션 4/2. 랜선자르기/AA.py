import sys
#sys.stdin = open("in1.txt", "rt")

k, n = map(int, input().split())
ls = []
for _ in range(k):
    a = int(input())
    ls.append(a)

f = 1
l = max(ls)

while f <= l:
    m = (f+l) // 2
    cnt = 0
    for e in ls:
        cnt += e // m
    if cnt >= n:
        f = m + 1
    else:
        l = m - 1

print(l)
