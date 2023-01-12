def find_least_sum_value_even(l):
    a, b = str(), str()
    for i in range(len(l)):
        if l[i] != '0':
            a, b = l[i], l[i + 1]
            l = l[:i] + l[i + 2:]
            break
    for i in range(0, len(l), 2):
        a += l[i]
        if i < len(l) - 1:
            b += l[i + 1]
    return a, b


while True:
    n = input()
    if n == '0': break
    li = sorted(n.split()[1:])
    if li[0] == 0:
        break
    n = li[0]
    # 짝수일때 홀수일때 나누면 될까?
    a, b = find_least_sum_value_even(li)

    print(int(a) + int(b))


