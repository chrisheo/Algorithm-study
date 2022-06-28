import sys


def is_plus(n):
    return True if abs(n) == n else False


def is_minus(n):
    return False if abs(n) == n else True


def findMinDiff(arr1, arr2):

    # Initialize difference as infinite
    diff = 10**20
    # Find the min diff
    for i in arr1:
        compare = i
        for j in range(len(arr2) - 1):
            if arr2[j] > i and arr2[j + 1] < i:
                k = min(abs(arr2[j] - i), abs(arr2[j + 1] - i))
                if k < diff:
                    diff = k
    # Return min diff, values
    return diff, temp1, temp2


N = int(input())
features = sys.stdin.readline().split()
# features convert to int from string
features = list(map(int, features))
features.sort()
# filter whether value is plus or minus
plus = list(filter(is_plus, features))
minus = list(filter(is_minus, features))

diff, value1, value2 = findMinDiff(minus, plus)
diff_p = plus[0] + plus[1]
diff_m = minus[len(minus) - 1] + minus[len(minus)-2]
# absolute to all variables to compare
diff = abs(diff)
diff_p = abs(diff_p)
diff_m = abs(diff_m)
if min(diff, diff_p, diff_m) == diff:
    print(value1, value2)
elif min(diff, diff_m, diff_p) == diff_p:
    print(plus[0], plus[1])
else:
    print(minus[len(minus) - 1] + minus[len(minus)-2])
