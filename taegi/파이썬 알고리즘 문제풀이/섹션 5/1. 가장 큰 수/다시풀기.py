'''가장큰수'''
# 13:27 -
import sys
sys.stdin = open("in1.txt","rt")

n, m = map(str,input().split())
m = int(m)
st = []
# 새로운 숫자가 기존 숫자보다 크고 & 제거할 숫자가 남아있으면
