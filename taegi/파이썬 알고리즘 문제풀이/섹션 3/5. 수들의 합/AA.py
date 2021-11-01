# 10:41 - 10:47 (6) 시간초과 (이중포문)
# 10:47 - 11:01 (14) 시간초과 x2 (?)
# 답확인

import sys
#sys.stdin = open("in1.txt","rt")

N,M = map(int,input().split())

ns = list(map(int,input().split()))



lt=0
rt=1
tot=ns[0]
cnt=0
while True:
    if tot<M: #M보다 작으면
        if rt<N: #오른쪽 포인터 끝까지 안갔으면
            tot+=ns[rt]
            rt+=1 #오른쪽 포인터 옮기고
        else:
            break
    elif tot==M:
        cnt+=1
        tot-=ns[lt]
        lt+=1
    else:
        tot-=ns[lt]
        lt+=1
print(cnt)


'''4,5번 시간초과'''
# answer=0
# s,e=0,1
# while True:
#     if s==N-1: break
#     tmp = sum(ns[s:e+1])
#     if tmp<M:
#         if e<N:
#             e+=1
#             continue
#     elif tmp==M:
#         answer+=1
#     s+=1
#     e=s+1
# print(answer)
