# 12:07 - 12:34 (27)
import sys
#sys.stdin = open("in1.txt","rt")

N = int(input())
mat = []
for _ in range(N):
    mat.append(list(map(int,input().split())))
#가장자리 0
#[1,1] ~ [n-2,n-2]
ans = 0
dx = [-1,0,1,0]
dy = [0,-1,0,1]
for i in range(N):
    for j in range(N):
        istop = mat[i][j]
        for k in range(4):
            if i+dx[k]>=0 and i+dx[k]<N and j+dy[k]>=0 and j+dy[k]<N:
                if istop <= mat[i+dx[k]][j+dy[k]]:
                    break
        else :
            #print("mat[%d][%d] = %d"%(i,j,mat[i][j]))
            ans+=1

print(ans)