# 16:06 - 16:28(22)
import sys

sys.stdin = open("in1.txt","rt")

N,M = map(int,input().split())
mat = list(map(int,input().split()))
mat.sort()
#print(mat)
s,e = 0,N-1
while s<e:
    m = (s+e)//2
    if mat[m]==M:
        break
    elif mat[m] < M:
        s = m+1
    else :
        e = m #왜 m이지..
print(m+1) #index라서 1더해줌