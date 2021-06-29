import sys
st = []
for i in range(int(sys.stdin.readline()),0,-1):
    st.append(i)
if len(st) == 1:
    print(st[0])
while len(st) > 1:
    print(st.pop())
    if len(st) == 1:
        print(st[0])
        break
    else:
        temp = [st.pop()]
        st = temp + st
