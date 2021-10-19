n=int(input())
lst=list(map(int, input().split()))
sum_list=[]

def digit_sum(x):
    sum=0
    for i in range(len(str(x))):
        sum+=int(str(x)[i])
    return sum

for x in lst:
    sum_list.append(digit_sum(x))
idx=sum_list.index(max(sum_list))
print(lst[idx])