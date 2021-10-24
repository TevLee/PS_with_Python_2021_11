'''역수열(그리디)'''
# 20:12 - 20:32 (20)
import sys
#sys.stdin = open("in1.txt","rt")

N = int(input())
ns = list(map(int,input().split())) #number
ns.insert(0,0)
res = [0]
# 역수열 -> 원래수열
# 뒤에서부터 오면서
# 자기보다 큰수잇으면 ns[i] 빼고 0되면 그위치에 insert
for n in range(N,0,-1):
    for i in range(len(res)):
        if ns[n]==0:
            res.insert(i,n)
            #print(res)
            break
        if n < res[i]:
            ns[n] -= 1
for i in range(len(res)-1):
    print(res[i],end=" ")


