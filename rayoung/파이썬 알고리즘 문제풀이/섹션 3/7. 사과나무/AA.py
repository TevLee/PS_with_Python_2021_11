import sys
#sys.stdin = open("in1.txt", "rt")

N = int(input())

s = 0
m = N // 2
for i in range(N):
    ls = list(map(int, input().split()))
    if i <= m:
        a = ls[m - i:m + i + 1]
    else:
        a = ls[i - m:N - i + m]
    s += sum(a)

print(s)
