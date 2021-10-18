# 18:15 - 18:24 (9)
import sys
#ys.stdin = open("in1.txt","rt")

N = int(input())
mat=[]

for _ in range(N):
    line = list(map(int,input().split()))
    mat.append(line)

#print(mat)
max = 0
#가로
for i in range(N):
    tmp = sum(mat[i])
    if tmp > max:
        max = tmp
#세로
for i in range(N):
    tmp = 0
    for j in range(N):
        tmp += mat[j][i]
    if tmp > max :
        max = tmp
#대각선
tmp = 0
for i in range(N):
    tmp +=mat[i][i]
if tmp > max:
    max = tmp
#대각선2
tmp = 0
for i in range(N) : #mat[0][n-1] ~ mat[n-1][0]
    tmp ++ mat[i][N-(i+1)]
if tmp>max:
    max = tmp
print(max)