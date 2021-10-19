t=int(input())

for j in range(t):
    n,s,e,k=map(int, input().split())
    lst=[]
    lst=input().split()
    lst=[int (i) for i in lst]
    lst=sorted(lst[s-1:e])
    print("#%d %d" %(j+1, lst[k-1]))