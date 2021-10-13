'''다른방법-211014-'''
#01:23 - 01:58 (35)
import sys
#sys.stdin = open("in1.txt","rt")

n,k = map(int,input().split())
#n개 카드입력
l = list(map(int,input().split()))
l.sort(reverse=True)
leng = len(l)
M = sum(l[0:3])
dp = [0]*(M+1)
for i in range(leng-2):
    for j in range(i+1,leng-1):
        for z in range(j+1,leng):
            m = l[i]+l[j]+l[z]
            dp[m]+=1

cnt = 0
for i in range(M,0,-1):
    if dp[i]!=0 :
        cnt+=1
        if cnt==k:
            print(i)
            break


