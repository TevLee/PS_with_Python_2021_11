import sys
#sys.stdin = open("in1.txt", "rt")

T = int(input())

for i in range(T):
    N, s, e, k = map(int, input().split())
    l = list(map(int, input().split()))
    m = l[s-1:e]
    m.sort()
    print("#{} {}".format(i+1, m[k-1]))
