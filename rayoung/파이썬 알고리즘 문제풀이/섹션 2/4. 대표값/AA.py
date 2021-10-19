import sys
#sys.stdin = open("in2.txt", "rt")

N = int(input())
l = list(map(int, input().split()))
avg = round(sum(l) / len(l))
num = 0
# re_p = abs(l[1] - avg)
gap = []
g = []
min = abs(l[1] - avg)

for i in range(N):
    gap.append(l[i] - avg)
    g.append(abs(l[i] - avg))

    if g[i] < min:
        min = g[i]
        num = i
    elif g[i] == min:
        if gap[i] > 0 and gap[num] < 0:
            min = g[i]
            num = i

print("{} {}".format(avg, num+1))
