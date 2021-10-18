import sys
#sys.stdin = open("in1.txt", "rt")

c = list(range(1, 21))

for i in range(10):
    a, b = map(int, input().split())
    s = c[a-1:b]
    c[a-1:b] = s[::-1]

for i in c:
    print(i, end=" ")
