# 18:38 - 19:00 (22) ##붙여넣기 실수
# 19:00 - 19:05 (5)
import sys
#sys.stdin = open("in1.txt","rt")

mat = []
for _ in range(9):
    mat.append(list(map(int,input().split())))

ans = "YES"

#가로 / 세로
for i in range(9):
    dp1 = [0] * 10
    dp2 = [0] * 10
    for j in range(9):
        dp1[mat[i][j]]+=1
        dp2[mat[j][i]]+=1
    # print(dp1)
    # print(dp2)
    if dp1.count(1) == 9 and dp2.count(1)==9:
        continue
    else :
        ans = "NO"
        break
#3x3
center = [[1,1],[1,4],[1,7],[4,1],[4,4],[4,7],[7,1],[7,4],[7,7]]
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
for i in range(len(center)):
    dp3 = [0]*10
    dp3[mat[center[i][0]][center[i][1]]]+=1
    for j in range(8):
        dp3[mat[center[i][0]+dx[j]][center[i][1]+dy[j]]]+=1
        # print(mat[center[i][0]+dx[j]][center[i][1]+dy[j]],end="")
    if dp3.count(1) == 9:
        continue
    else:
        ans = "NO"
        break
print(ans)
