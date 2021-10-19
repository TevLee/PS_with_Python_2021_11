#01:15 - 01:22 (7)
import sys
#sys.stdin = open("in1.txt","rt")
tc = int(input())

for t in range(tc):
    n,s,e,k = map(int,input().split())
    l = list(map(int,input().split()))
    l = l[s-1:e]
    l.sort()
    print(f"#{t+1} {l[k-1]}")
