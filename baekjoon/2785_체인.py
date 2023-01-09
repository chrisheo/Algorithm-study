from sys import stdin

n = int(stdin.readline())

lengths = list(map(int, stdin.readline().split()))

numOfOne = lengths.count(1)
#1개의 개수
count = 0

while True:
    if n == 1:
        break
    if n == numOfOne:
        n -= 2
        count += 1
        numOfOne -= 3
    else:
        if n - numOfOne >= 2 and numOfOne >= 1:
            count += 1
            n -= 2
            numOfOne -= 1
        else:
            count += 1
            n -= 1

print(count)