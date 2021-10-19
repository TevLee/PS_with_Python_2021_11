import sys
#sys.stdin = open("in1.txt", "rt")

d = []
n, k = map(int, input().split())

for i in range(1, n+1):
    if n % i == 0:
         d.append(i)

if len(d) >= k:
    print(d[k-1])
else:
    print(-1)
