'''공주구하기(큐)'''
# 14:04 - 14:12 (8)
import sys
from collections import deque
#sys.stdin = open("in1.txt","rt")

N,K = map(int,input().split())
deq = deque()
for i in range(1,N+1):
    deq.append(i)
#입력
while len(deq)>1:
    for k in range(K-1): # K-1번 돌아야 남아있는 왕자가 K를 외침
        p = deq.popleft() #prince
        deq.append(p)
    deq.popleft()
    # print(deq)
print(deq[0])
