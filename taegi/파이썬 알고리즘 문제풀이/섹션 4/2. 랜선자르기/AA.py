# 17:31 - 18:01 (30)
import sys
#sys.stdin = open("in3.txt","rt")

K,N = map(int,input().split()) #K<=N
ns = []
for _ in range(K):
    ns.append(int(input()))
ns.sort()

s,e = 0,ns[-1]
while s<=e:
    m = (s+e)//2
    cnt = 0
    for n in ns:
        cnt += n//m
    #print(n,m,cnt)
    if cnt>=N:
        ans = m
        s = m+1
    else :
        e = m-1
print(ans)

