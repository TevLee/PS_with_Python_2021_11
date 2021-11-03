# 23:03 - 23:36 (33)
import sys

#sys.stdin = open("in"+str(i)+".txt","rt")

N,M = map(int,input().split())
# N개 곡 순서대로, M개 DVD에 M은 같은 크기
#DVD 최소 용량 크기
ts = list(map(int,input().split())) #times
# 입력
s,e = 0,sum(ts) #end는 노래길이의 총합

ans = 0
while s<e:
    m = (s+e)//2
    t = 0
    dvd = 1
    for i in range(len(ts)):
        t+=ts[i]
        if t>m: # 시간 합이 mid넘으면 
            dvd+=1 # -> dvd추가
            t=ts[i] # 새 dvd에 i번째 곡 추가
    if dvd <= M:# dvd 갯수가 M보다 작거나 같으면
        ans = m
        e = m # 현재 갯수가 답이 될 수도 있으므로 m-1이 아니라 m
    elif dvd > M:
        s = m+1
print(m+1) ##
'''모범답안
while lt<=rt:
    mid=(lt+rt)//2
    if mid>=maxx and Count(mid)<=m: #조건을 2개 걸었음
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)
'''