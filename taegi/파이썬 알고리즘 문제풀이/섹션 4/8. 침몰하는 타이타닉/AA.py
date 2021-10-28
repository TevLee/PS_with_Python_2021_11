'''침몰하는 타이타닉(그리디)'''
# 21:38 - 22:01 (23) # 작은 것끼리 먼저 더했음
# 22:01 - 22:07 (6)
import sys
#sys.stdin = open("in5.txt","rt")
# 구명보트 2명 이하 & M kg 이하

N,M = map(int,input().split()) # 자연수
# N 몸무게 50-150 <=M
ws = list(map(int,sys.stdin.readline().split()))
ans = 0 # 최소 구명보트 갯수
# 입력
ws.sort()

l,r = 0,N-1
while l<=r:
    onBoat = ws[l]+ws[r] #보트에 탄 사람 몸무게 합이
    if onBoat > M:
        ans +=1
        r-=1 #무거운애만 혼자태워보냄
    else : # M보다 가벼우면
        ans +=1
        r-=1
        l+=1
print(ans)