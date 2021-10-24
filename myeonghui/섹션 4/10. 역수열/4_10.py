n=int(input())
lst=list(map(int,input().split()))

ch=[]
lst=lst[::-1]

for i in lst:
    ch.insert(i,n)
    n-=1
for j in ch:
    print(j, end=' ')
