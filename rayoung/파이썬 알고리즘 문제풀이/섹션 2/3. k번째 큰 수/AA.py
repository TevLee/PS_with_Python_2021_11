import sys
#sys.stdin = open("in1.txt", "rt")

N, K = map(int, input().split())
l = list(map(int, input().split()))

r = []

for a in range(N-2):
    x = l[a]
    for b in range(a+1, N-1):
        y = l[b]
        for c in range(b+1, N):
            z = l[c]
            r.append(x+y+z)

result = list(set(r))
result.sort(reverse=True)
print(result[K-1])
