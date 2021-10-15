# 03:46 - 04:03 (17)
import sys
#sys.stdin = open("in4.txt","rt")

N = int(input())
ns = list(map(int,input().split()))
# 뒤집고 소수면, 출력
def reverse(x):
    return int(str(x)[::-1])

def isPrime(x):
    if x == 1:
        return False
    for i in range(2,x):
        if x%i == 0 :
            return False
    return True
for n in ns:
    rn = reverse(n)
    if isPrime(rn) == True:
        print(rn,end=" ")