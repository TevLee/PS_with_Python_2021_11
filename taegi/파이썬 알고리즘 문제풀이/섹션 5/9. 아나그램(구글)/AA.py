'''아나그램(딕셔너리)'''
# 14:03 - 14:10 (7)
import sys
#sys.stdin = open("in5.txt","rt")

ws = list(input())
dic = {}
for w in ws:
    if w in dic:
        dic[w]+=1
    else :
        dic[w]=1
print(dic)
ws2 = list(input())
for w in ws2:
    if w not in dic:
        print("NO")
        break
    elif dic[w]==0:
        print("NO")
        break
    else :
        dic[w]-=1
else:
    print("YES")
'''
<개선된 코드>
import sys
#sys.stdin=open("in1.txt", "r")
a=input()
b=input()
sH=dict()
for x in a:
    sH[x]=sH.get(x, 0)+1
for x in b:
    sH[x]=sH.get(x, 0)-1

for x in a:
    if(sH.get(x)>0):
        print("NO")
        break;
else:
    print("YES")
'''