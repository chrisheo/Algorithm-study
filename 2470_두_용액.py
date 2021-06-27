import sys

def is_plus(n):
    return True if abs(n) == n else False
def is_minus(n):
    return False if abs(n) == n else True
N = int(input())
features = sys.stdin.readline().split()
#features convert to int from string
features = list(map(int, features))
#filter whether value is plus or minus
plus = list(filter(is_plus, features))
minus = list(filter(is_minus, features))

