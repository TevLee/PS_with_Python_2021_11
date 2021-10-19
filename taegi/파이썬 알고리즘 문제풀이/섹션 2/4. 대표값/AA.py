# 02:00 - 02:17 (17)
import sys
#sys.stdin = open("in1.txt","rt")

n = int(input())
ms = list(map(int,input().split()))
#ms의 평균 #가장가까운 학생 몇번째?
mean = round(sum(ms)/n,0)

errors = [abs(round(m-mean,0)) for m in ms]
min = min(errors)
answer = 0
#앞에서부터 찾으면서 min이면 넣고, min이면서 평균보다 크면 교체
for i in range(len(ms)):
    if errors[i]==min:
        if ms[i]>=mean:
            answer = i
            break
        answer = i
print("%d %d" %(mean,answer+1))