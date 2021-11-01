# 15:46 - 16:00 (14)
import sys
from collections import deque
#sys.stdin = open("in1.txt","rt")

mat = []
for _ in range(7):
    mat.append(list(map(int,input().split())))
ans = 0

for i in range(7):
    for j in range(3):
        deq = deque()
        deq.extend(mat[i][j:j+5])
        r,l = deq.popleft(),deq.pop()
        if r!=l:continue
        r, l = deq.popleft(), deq.pop()
        if r==l :
            #print(deq)
            ans+=1
nmat = list(map(list,zip(*mat)))
for i in range(7):
    for j in range(3):
        deq = deque()
        deq.extend(nmat[i][j:j+5])
        r,l = deq.popleft(),deq.pop()
        if r!=l:continue
        r, l = deq.popleft(), deq.pop()
        if r==l :
            # print(deq)
            ans+=1
print(ans)
[1,2,3]
[4,5,6]

[1,4]
[2,5]
[3,6]
