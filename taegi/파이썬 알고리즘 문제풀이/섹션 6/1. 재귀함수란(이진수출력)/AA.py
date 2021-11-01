'''재귀함수를 이용한 이진수 출력'''
# 13:28 - 13:38(10)
import sys
#sys.stdin = open("in1.txt","rt")

def func(n):
    if n<=1:
        return str(n)
    else :
        return str(func(n//2))+str(n%2)

n=int(input())
print(func(n))