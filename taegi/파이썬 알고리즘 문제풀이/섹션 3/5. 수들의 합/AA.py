# 10:41 - 10:47 (6) 시간초과 (이중포문)
# 10:47 - 11:01 (14) 시간초과 x2 (?)

import sys
#sys.stdin = open("in1.txt","rt")

N,M = map(int,input().split())

ns = list(map(int,input().split()))

answer=0


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
