# 10:18 - 10:28 (10)
import sys
#sys.stdin = open("in1.txt","rt")

cards = [i for i in range(21)] #0,1~

for _ in range(10):
    s,e = map(int,input().split())
    l = e-s+1 #s-e아니고 e-s
    for j in range(l//2): # 4면 1, 5면 1까지
        cards[s+j],cards[e-j] = cards[e-j],cards[s+j]
    #print(cards[1:])
for n in cards[1:]:
    print(n,end=" ")