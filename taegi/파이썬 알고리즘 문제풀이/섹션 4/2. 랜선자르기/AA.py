# 17:31 - 18:01 (30)
## 풀이법 모범답안과 동일
import sys
#sys.stdin = open("in3.txt","rt")

K,N = map(int,input().split()) #K<=N
ns = []
for _ in range(K):
    ns.append(int(input()))
ns.sort()
# 입력
s,e = 0,ns[-1] #end는 가장 큰값
while s<=e:
    m = (s+e)//2
    cnt = 0
    for n in ns:
        cnt += n//m # mid값으로 획득할 수 있는 랜선 갯수를 각각 구해서 더함
    if cnt>=N: # 원하는 랜선 갯수(N)보다 많으면 ## N과 같으면
        ans = m
        s = m+1 # -> mid 값을 크게 만듬 ## while문 False
    else :
        e = m-1
print(ans)

