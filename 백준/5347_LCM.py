n = int(input())


def lcm(a, b):
    if b == 0:
        return a
    return lcm(b, a % b)


for _ in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    print(int(a * b / lcm(a, b)))
