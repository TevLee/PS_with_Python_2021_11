# 11:10 - 12:04 (54)
import sys
#sys.stdin = open("in3.txt","rt")

N = int(input()) # 홀수
mat = []
for _ in range(N):
    mat.append(list(map(int, input().split())))

#회전
M = int(input())
for _ in range(M):
    n,r,c = map(int,input().split())#nth, right,cnt
    if c>=N: c = c%N #테스트 3,4
    tmp = []
    if r == 1: #오른쪽
        mat[n-1] = mat[n-1][-c:]+mat[n-1][:-c]
        #print(mat[n-1])
    elif r == 0:
        mat[n-1] = mat[n-1][c:]+mat[n-1][:c]
        #print(mat[n-1])
#print("\n")
#다이아몬드 합
ans = 0
m = N//2
for i in range(m+1):
    #print(mat[i][i:N-i])
    ans += sum(mat[i][i:N-i])
for j in range(1,m+1):
    #print(mat[m+j][m-j:m+j+1])
    ans += sum(mat[m+j][m-j:m+j+1])

print(ans)