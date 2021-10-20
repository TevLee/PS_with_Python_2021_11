# 23:03 - 23:36 (33)
import sys

#sys.stdin = open("in"+str(i)+".txt","rt")

N,M = map(int,input().split())
# N개 곡 순서대로, M개 DVD에 M은 같은 크기
#DVD 최소 용량 크기
ts = list(map(int,input().split())) #times
s,e = 0,sum(ts)

ans = 0
while s<e:
    m = (s+e)//2
    t = 0
    dvd = 1
    for i in range(len(ts)):
        t+=ts[i]
        if t>m:
            dvd+=1
            t=ts[i]
    if dvd <= M:#dvd개수 늘려야 = dvd 크기 줄여야
        ans = m
        e = m ###왜m?
    elif dvd > M:
        s = m+1
print(m+1) ###왜m+1?
