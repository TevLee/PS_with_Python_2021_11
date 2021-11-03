'''알리바바와 40인의 도둑(Bottom-Up)'''
#12:45 - 13:01 (16)

import sys
#sys.stdin = open("in1.txt","rt")
N = int(input()) # <=20
ns = [list(map(int,input().split())) for _ in range(N)]
# dp =[ns[0]]
# for _ in range(N-1):
#     dp.append([0]*N)
for i in range(1,N): #왼쪽 라인 더해주고
    ns[i][0] += ns[i-1][0]
    ns[0][i] += ns[0][i-1]
for i in range(1,N):
    for j in range(1,N):
        ns[i][j] += min(ns[i-1][j],ns[i][j-1])
# for i in range(N):
#     print(ns[i])
print(ns[N-1][N-1])