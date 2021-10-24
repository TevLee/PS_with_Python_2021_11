n,m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

lt = 0
rt = len(lst) - 1
mid = (lt+rt) // 2

while lst[mid] != m
    mid = (lt+rt) // 2

    if a[mid] == m:
        print(mid + 1)
        break
    elif a[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1

print(cnt)


