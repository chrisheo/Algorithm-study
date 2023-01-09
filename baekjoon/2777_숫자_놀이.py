from sys import stdin

n = int(input())
values = []

def findX(value):
    X_length = 0
    count7 = 0
    count5 = 0
    count3 = 0
    count2 = 0
    wrong = False
    while True:
        if value % 7 == 0:
            value /= 7
            count7 += 1
        elif value % 5 == 0:
            value /= 5
            count5 += 1
        elif value % 3 == 0:
            value /= 3
            count3 += 1
        elif value % 2 == 0:
            value /= 2
            count2 += 1
        elif value == 1:
            break
        else:
            wrong = True
            break
    if wrong:
        return -1
    else:
        X_length += count7
        X_length += count5
        X_length += count3 // 2
        if count3 % 2 != 0:
            X_length += 1
        X_length += count2 // 3
        if count2 % 3 != 0:
            X_length += 1

        return X_length


for i in range(n):
    values.append(int(stdin.readline()))

for value in values:
    print(findX(value))
()