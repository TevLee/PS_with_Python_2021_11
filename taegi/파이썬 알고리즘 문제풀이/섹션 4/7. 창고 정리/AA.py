'''창고정리'''
# 21:30 - 21:33 (3)
import sys
#sys.stdin = open("in1.txt","rt")

L = int(sys.stdin.readline()) # 1~100
bs = list(map(int,input().split())) #box
M = int(sys.stdin.readline())

for _ in range(M):
    bs[ bs.index(max(bs)) ] -=1 #가장높은애 내리고
    bs[ bs.index(min(bs)) ] +=1 #가장낮은애 주고
print(max(bs)-min(bs))