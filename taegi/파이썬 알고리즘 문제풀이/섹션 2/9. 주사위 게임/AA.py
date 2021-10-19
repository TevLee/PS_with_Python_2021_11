# 04:06 - 04:14 (8)
import sys
#sys.stdin = open("in1.txt","rt")

N = int(input())
max = 0
# 주사위 3개
# 10000 + n*1000
# 1000 + n*100
# max*100

for _ in range(N):
    ns = list(map(int,input().split()))
    ns.sort()
    cnt = ns.count(ns[-1]) #가장큰수 갯수
    if cnt==3: gold = 10000+ ns[-1]*1000
    elif cnt==2: gold = 1000 + ns[-1]*100
    else : gold = ns[-1]*100
    if gold > max:
        max = gold
print(max)
