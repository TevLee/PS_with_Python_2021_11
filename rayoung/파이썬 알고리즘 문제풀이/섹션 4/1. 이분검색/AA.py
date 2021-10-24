import sys
#sys.stdin = open("in1.txt", "rt")

N, M = map(int, input().split())
ls = list(map(int, input().split()))
ls.sort()

f = 0
l = N-1

while f <= l:
    mid = (f + l) // 2
    if ls[mid] == M:
        print(mid+1)
        break
    elif ls[mid] < M:
        f = mid + 1
    else:
        l = mid - 1
