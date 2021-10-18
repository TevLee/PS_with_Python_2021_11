import sys
#sys.stdin = open("in1.txt", "rt")

N = int(input())
for i in range(N):
    s = str(input()).lower()
    if s == s[::-1]:
        print("#{} YES".format(i+1))
    else:
        print("#{} NO".format(i+1))
