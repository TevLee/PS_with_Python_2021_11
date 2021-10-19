import sys
#sys.stdin = open("in5.txt", "rt")

N = int(input())
ls = []
w = []

for i in range(N):
    l = list(map(int, input().split()))
    ls.append(l)
    w.append(sum(l))

h = []
d1 = 0
d2 = 0
d = []

for i in range(N):
    height = 0
    for j in range(N):
        height += ls[j][i]
        if j == i:
            d1 += ls[i][j]
        elif j == (N -i -1):
            d2 += ls[i][j]
    h.append(height)

m = [max(w), max(h), d1, d2]
print(max(m))
