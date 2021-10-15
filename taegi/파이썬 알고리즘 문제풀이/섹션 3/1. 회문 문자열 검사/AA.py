#09:37 - 10:01 (24)
import sys
#sys.stdin = open("in3.txt","rt")

# 문자열 팰린드롬이면 Yes
def Ispal(s):
    s=s.lower()
    for i in range(len(s)//2): #4면 1, 5면 1, 6이면 2까지
        if s[i] != s[-(i+1)]:
            return False
    else:
        return True

# 대소문자구분x
N = int(input())
for i in range(N):
    s = str(input())
    if Ispal(s) == True: print(f"#{i+1} YES")
    else : print(f"#{i+1} NO")