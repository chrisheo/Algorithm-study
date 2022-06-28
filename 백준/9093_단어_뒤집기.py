import sys

N = int(input())


def printer(l):
    l.reverse()
    print(''.join(l), end=' ')
    l.clear()


for i in range(N):
    line = sys.stdin.readline()
    l = []
    s = 0
    while line[s] != '\n':
        l.append(line[s])
        s += 1
        if line[s] == ' ':
            printer(l)
            s += 1
    printer(l)
