import sys
#sys.stdin = open("in1.txt", "rt")

N = int(input())
num = list(map(int, input().split()))

ls = []

for e in num:
    s = sum(map(int, str(e)))
    ls.append(s)

max = 0

for i in range(N):
    if ls[i] > max:
        max = ls[i]
        result = num[i]

print(result)
