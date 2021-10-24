# 00:11 - 00:19 (8)
import sys
#sys.stdin = open("in1.txt","rt")

N = int(sys.stdin.readline()) #선길이
# 1m,2m로 절단
dp = [0]*(N+1)
dp[1]=1
dp[2]=2
for i in range(3,N+1):
    dp[i] = dp[i-2]+dp[i-1] # i-2에서 +2m / i-1에서 +1m
print(dp[N])
