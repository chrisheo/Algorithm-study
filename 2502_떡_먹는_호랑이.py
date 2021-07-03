d,k = input().split()
d = int(d)
k = int(k)
def rev_pivo(day,first,second):
    if day == 3:
        print(first)
        print(second)
        return
    else:
        temp = first
        first = second - first
        second = temp
        if first > second:
            return -1
        return rev_pivo(day - 1,first,second)
for i in range(int(k/2),0,-1):
    if rev_pivo(d,i,k-i) != -1:
        break

    