N,K = map(int, input().split())
lst=list(map(int, input().split()))
sum_lst=set()


for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum_lst.add(lst[i]+lst[j]+lst[k])
sum_lst=list(sum_lst)
sum_lst.sort(reverse=True)
print(sum_lst[K-1])