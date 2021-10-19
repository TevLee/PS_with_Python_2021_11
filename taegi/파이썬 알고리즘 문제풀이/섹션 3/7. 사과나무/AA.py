# 18:26 - 18:53 (27)
import sys
#sys.stdin = open("in1.txt","rt")

N = int(input()) #홀수 N-> N//2+1이 중앙
mat = []
for _ in range(N):
    line = list(map(int,input().split()))
    mat.append(line)

m = N//2 # 5일때 2
ans = 0
#삼각형
for i in range(m+1):
    #print(mat[i][m-i:m+i+1])
    ans += sum(mat[i][m-i:m+i+1])
#역삼각형
for j in range(1,m+1):
    #print(mat[m+j][j:N-j])
    ans += sum(mat[m+j][j:N-j])
print(ans)