def DFS(L, s):
    global cnt
    if L==m:
        for i in range(m):
            print(res[i], end=' ')
        print()
        cnt+=1
    else:
        for i in range(s, n+1):
            res[L]=i
            # s(시작점)가 아닌 i(뻗어나가는 가지)에 +1
            DFS(L+1, i+1)


n, m=map(int, input().split())
res=[0]*(n+1)
cnt=0
DFS(0, 1)
print(cnt)
