import sys
#sys.stdin = open("in4.txt", "rt")

N, M = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0

for i in range(N):
    s = A[i]
    if s >= M:
        continue
    else:
        for j in range(i+1, N):
            s += A[j]
            if s == M:
                cnt += 1
            elif s > M:
                break

print(cnt)

#5번 time limit
