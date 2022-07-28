#set으로 푸는 방법도 생각나지만 이진 탐색으로 먼저 시도
N = int(input())
stock = list(map(int, input().split()))

M = int(input())
offer = list(map(int, input().split()))

stock.sort()
#재귀로 구현
def binary_search_recursion(target, start, end, data):
    if start > end:
        return None

    mid = (start + end) // 2

    if data[mid] == target:
        return mid
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1        

    return binary_search_recursion(target, start, end, data)

for i in offer:
  result = binary_search_recursion(i,0,N-1, stock)
  if result == None:
    print('no', end = ' ')
  else:
    print('yes', end = ' ')