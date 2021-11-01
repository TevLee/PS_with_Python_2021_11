#8'
#진우-선우
import sys
from collections import deque
j,s = map(int,input().split())# 진우, 선우
d = int(input()) # day
tot = j+s
for i in range(1,d+1):
    if i%2==1:#홀수 : j-
        j = j//2
        s = tot-j
    else : #짝수 : j+
        s = s//2
        j = tot-s
print(j,s)


#100 100 4
#131 69
#1 1 9
#1 1