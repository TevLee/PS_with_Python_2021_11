#25'
#거울단어
import sys
from collections import deque
N = int(input())
#ws = []
ws = [sys.stdin.readline().strip() for i in range(N)]
print(ws)
#print(N,l)
m = {'d':'b','b':'d','i':'i','l':'l','m':'m','n':'n','o':'o','p':'q',\
     'q':'p','s':'z','z':'s','u':'u','v':'v','w':'w','x':'x'}
for w in ws:
    deq = deque()
    deq.extend(w)
    while True:
        r, l = deq.popleft(), deq.pop()
        if len(deq)<=1:
            print("Mirror")
            break
        if r in m:
            if m[r]==l:
                continue
            else:
                print("Normal")
                break

#    print(deq)
'''
3
popooqoq
bvdobvd
banana
'''
'''
Mirror
Mirror
Normal
'''