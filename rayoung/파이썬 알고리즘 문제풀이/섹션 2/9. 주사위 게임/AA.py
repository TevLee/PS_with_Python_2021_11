import sys
#sys.stdin = open("in1.txt", "rt")

N = int(input())
m = 0
money = []

for i in range(N):
    l = list(map(int, input().split()))
    l.sort()
    p, q, r = map(int, l)
    if p == q == r:
        m = 10000 + (p * 1000)
    elif p == q or q == r:
        m = 1000 + (q * 100)
    elif p == r:
        m = 1000 + (p * 100)
    else:
        m = r * 100
    money.append(m)

print(max(money))
