N = int(input())
l = []
l_rev = []


def is_pal(num):
    num = str(num)
    length = len(num)
    boo = True
    for i in range(int(length / 2)):
        if num[i] != num[length - i - 1]:
            boo = False
            break
    if boo:
        print("YES")
    else:
        print("NO")


for i in range(N):
    l.append(input())
    l_rev.append(l[i][::-1])
    num = int(l[i]) + int(l_rev[i])
    is_pal(num)
