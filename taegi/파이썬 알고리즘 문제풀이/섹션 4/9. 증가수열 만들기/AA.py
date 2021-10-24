'''모범풀이 확인...'''
'''증가수열 만들기(그리디)'''
# 21:35 - 22:08 (33)
import sys
#sys.stdin = open("in3.txt", "rt")

N = int(input())
ns = list(map(int,input().split())) #number
d = "" #direction
ans = 0
n,l,r = 0,0,N-1

while True:
    if l==r:
        if n < ns[l] :
            ans+=1
            d+="L"
            break
    if n > ns[l] and n > ns[r] : #l,r < n
        break
    elif ns[l]<ns[r] :
        if n < ns[l]: # n < l < r
            n = ns[l]
            l+=1
            d+="L"
        elif n<ns[r]: # l < n < r
            n = ns[r]
            r-=1
            d+="R"
        ans+=1
    else :
        if n<ns[r]: # n < r < l
            n = ns[r]
            r-=1
            d+="R"
        elif n<ns[l]: #   r < n < l
            n = ns[l]
            l+=1
            d+="L"
        ans+=1
print(ans)
print(d)





