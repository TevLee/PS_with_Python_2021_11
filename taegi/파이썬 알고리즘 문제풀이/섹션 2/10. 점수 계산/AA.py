# 04:14 -
import sys
#sys.stdin = open("in1.txt","rt")

N = int(input()) # 100이하
rs = list(map(int,input().split()))
# k번연속 정답이면 k점
dp = [0]*N
dp[0]=rs[0] #첫문제채점
for i in range(1,len(rs)):
    if rs[i-1]==1:#앞문제맞았으면
        if rs[i]==1: #이번문제도 맞았으면
            dp[i]=dp[i-1]+1
    else : #앞문제 틀렸으면
        dp[i]=rs[i]
#print(dp)
answer = sum(dp)
print(answer)
