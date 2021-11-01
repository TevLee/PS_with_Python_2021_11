#3:31 -
#모음만 알아듣는 앵무새
import sys
N = int(input()) # 1~100
ws = [sys.stdin.readline().strip() for _ in range(N)] #words 1~255
mos = ['a','e','i','o','u','A','E','I','O','U'] #모음s
for w in ws:
    # if all(i not in mos for i in w): #모음없으면
    #     print("???")
    # else :
    #     mo = ""
    #     for alpha in w:
    #         if alpha in
    res = []
    for i in w:
        if i in mos :
            res.append(i)
    if len(res)==0:
        print("???")
    else :
        print("".join(res))

'''
4
Hello, World!
I'm your father.
What are you doing here?
bcd
'''
'''
eoo
Iouae
aaeouoiee
'''