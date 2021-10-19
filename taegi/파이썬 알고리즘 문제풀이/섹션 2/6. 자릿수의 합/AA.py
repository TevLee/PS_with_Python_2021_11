#02:57 - 13:20 (23)
#03:21 - 03:26 (5)
import sys
#sys.stdin = open("in2.txt","rt")

N = int(input()) # 100만 이하
ns = list(map(int,input().split()))
ns.reverse()
# 각자릿수의 합, 합이 최대인 n
## 합이 같으면 먼저 입력
def digit_sum(n):
    sum = 0
    while n>0:
        sum += n%10
        n = n//10
    return sum

max = 0
for i in range(len(ns)):
    ds = digit_sum(ns[i])
    if ds>=max :
        max = ds
        answer = i
print(ns[answer])
