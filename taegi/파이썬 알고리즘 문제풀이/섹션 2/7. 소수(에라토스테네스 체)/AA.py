#03:27 - 03:43 (16)
import sys
#sys.stdin = open("in3.txt","rt")

N = int(input())
dp = [0]*(N+1)
# N까지 소수의 갯수
for i in range(2,int(N**0.5)+1):
    if dp[i] == 0:
        for j in range(i*2,N+1,i):
            dp[j]=1
answer = dp.count(0)-2 # 0,1 제외
print(answer)