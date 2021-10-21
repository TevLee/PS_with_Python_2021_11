import sys
#sys.stdin = open("in1.txt", "rt")

ls= []

for _ in range(7):
    l = list(map(int, input().split()))
    ls.append(l)

cnt = 0
for i in range(3):
    for j in range(7):
        if ls[i][j] == ls[i+4][j] and ls[i+1][j] == ls[i+3][j]:
            cnt += 1
        if ls[j][i] == ls[j][i+4] and ls[j][i+1] == ls[j][i+3]:
            cnt += 1

print(cnt)
