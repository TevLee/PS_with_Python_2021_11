'''후위식 연산'''
# 13:52 - 14:02 (10)
import sys
#sys.stdin = open("in"+str(i)+".txt","rt")

N = input()
st = []
for x in N:
    if x.isdecimal():
        st.append(x)
    else: #문자면
        a = int(st.pop())
        b = int(st.pop())
        if x=="(":
            st.append(x)
        elif x== '+':
            st.append(a+b)
            #print(a+b,end=" ")
        elif x=='-':
            st.append(b-a)
            #print(b-a,end=" ")
        elif x=="*":
            st.append(a*b)
            #print(a*b,end=" ")
        elif x=="/":
            st.append(b/a)
            #print(a//b,end=" ")
print(st[0])
