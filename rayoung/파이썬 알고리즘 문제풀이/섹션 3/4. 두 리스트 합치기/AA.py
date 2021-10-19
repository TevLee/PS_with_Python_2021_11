import sys
#sys.stdin = open("in1.txt", "rt")

N = int(input())
ln = list(map(int, input().split()))
M = int(input())
lm = list(map(int, input().split()))
ls = ln + lm
ls.sort()
for i in ls:
    print(i, end=" ")
