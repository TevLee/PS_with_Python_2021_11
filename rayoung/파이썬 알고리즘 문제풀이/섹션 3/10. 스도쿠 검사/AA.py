import sys
#sys.stdin = open("in3.txt", "rt")

ls = []

for _ in range(9):
    l = list(map(int, input().split()))
    ls.append(l)

result = "YES"

for i in range(9):
    c1 = [0] * 10
    c2 = [0] * 10
    for j in range(9):
        c1[ls[i][j]]=1
        c2[ls[j][i]]=1
    if sum(c1)!=9 or sum(c2)!=9:
        result = "NO"

for i in range(3):
    for j in range(3):
        c3 = [0] * 10
        for k in range(3):
            for m in range(3):
                c3[ls[(i * 3) + k][(j * 3) + m]]=1
        if sum(c3)!=9:
            result = "NO"

print(result)
