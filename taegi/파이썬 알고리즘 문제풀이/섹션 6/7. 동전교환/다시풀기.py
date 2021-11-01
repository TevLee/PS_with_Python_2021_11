'''동전교환'''
# 13:45 - 13:54 ## 완전탐색 x
# DFS
import sys
sys.stdin = open("in3.txt","rt")

n = int(input())
cs = list(map(int,input().split()))
m = int(input())
cs.sort(reverse=True)
ans=0


