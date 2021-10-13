# 02:18 - 02:25 (7)
import sys
#sys.stdin = open("in1.txt","rt")

N,M = map(int,input().split()) #4,6,8,12,20
answer = 0
# N,M면체 주사위 눈의 합 중 최대확률 숫자
## 여러개면 오름차순
total = N*M
dp = [0]*(total+1)

for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i+j]+=1
max = max(dp)
c = dp.count(max)
if c>1:
    for i in range(len(dp)):
        if dp[i]==max:
            print(i,end="")
            c-=1
            if c==0: break
            print(" ",end="")
else :
    print(dp.index(max))
