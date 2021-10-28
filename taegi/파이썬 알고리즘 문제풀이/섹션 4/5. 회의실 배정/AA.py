'''회의실배정 (그리디)'''
# 00:11 - 00:20 (9)
import sys
#sys.stdin = open("in1.txt","rt")

N = int(sys.stdin.readline())
rs = []#rooms
ans = [0,0] # 회의수,끝나는시간
for _ in range(N):
    rs.append(list(map(int,input().split())))
# 입력
rs.sort(key=lambda x:x[1]) # rs의 1번째 인덱스 값으로 정렬...
for r in rs:
    if ans[1]<=r[0]: #앞 회의종료시간이 r 회의시간 시작과 작거나 같으면
        ans[0]+=1
        ans[1]=r[1]
print(ans[0])
