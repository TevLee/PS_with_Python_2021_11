import sys
#sys.stdin = open("in1.txt", "rt")

N = int(input())
ls = list(map(int, input().split()))
cnt = 0
scr = 0

for l in ls:
    if l == 1:
        cnt += 1
        scr += cnt
    else:
        cnt = 0

print(scr)
