'''단어찾기'''
#13:56 - 14:02(6)
import sys
#sys.stdin = open("in1.txt","rt")

n = int(input()) #3~100
keys = [str(input().strip()) for _ in range(n)]
dic = {}
for i in range(n):
    dic[keys[i]]=1
for j in range(n-1):
    j = str(input().strip())
    dic[j]-=1
for k in range(n):
    if dic[keys[k]]==1:
        print(keys[k])