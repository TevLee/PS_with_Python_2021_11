import sys
sys.stdin = open("in1.txt","rt")

n=int(input())
res = 0
for _ in range(n):
    tmp = list(map(int, input().split()))
    tmp.sort()
    a,b,c = map(int, tmp)
    if a==b and b==c:
        money = 10000 + c*1000
    elif a==b and a!=c:
        money = 1000 + (a*100)
    elif a!=b and b==c:
        money = 1000 + (b*100)
    else:
        money = c*100
    if money > res:
        res = money
print(res)
