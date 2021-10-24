import sys
#sys.stdin = open("in1.txt", "rt")

ls = []

N = int(input())
for _ in range(N):
    l = list(map(int, input().split()))
    l.insert(0, 0)
    l.append(0)
    ls.append(l)

ls.insert(0, [0] * (N+2))
ls.append([0] * (N+2))

cnt = 0

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if ls[i][j] > ls[i-1][j] and ls[i][j] > ls[i+1][j] and ls[i][j] > ls[i][j-1] and ls[i][j] > ls[i][j+1]:
            cnt += 1

print(cnt)
