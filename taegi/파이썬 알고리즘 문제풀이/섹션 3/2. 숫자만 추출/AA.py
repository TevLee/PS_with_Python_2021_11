# 10:04 - 10:13 (9)
import sys
#sys.stdin = open("in2.txt","rt")

s = str(input())
#숫자만 추출해서 자연수 + 자연수의 약수개수
#0무시
l = []
for i in s:
    if i >='0' and i<='9':
        l.append(i)
ll = int("".join(l))

cnt=0
for i in range(1,ll+1):
    if ll%i == 0:
        cnt +=1
print(ll)
print(cnt)