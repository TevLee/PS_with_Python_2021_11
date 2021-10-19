# 10:31 - 10:35 (4)
import sys
#sys.stdin = open("in1.txt","rt")

N = int(input())
ns = list(map(int,input().split())) #오름차순
M = int(input())
ms = list(map(int,input().split())) #오름차순

l = sorted(ns+ms)
for i in l:
    print(i,end=" ")
