#25'
import sys

N,M = map(int,sys.stdin.readline().split())
mat = []

row = ["#"]*M
rend = ["."]*(M-1)+["#"]
lend = ["#"]+["."]*(M-1)
mat.append(row if i%2==0 else rend if i%4==1 else lend for i in range(N))
# for i in range(N):
#     if i%2==0:
#         mat.append(row)
#     elif i%4==1:
#         mat.append(rend)
#     else :
#         mat.append(lend)
for i in mat:
    for j in i:
        print(j,end="")
    print()