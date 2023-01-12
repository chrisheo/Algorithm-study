#https://www.acmicpc.net/problem/11501
import sys
n_test = int(sys.stdin.readline())
for _ in range(n_test):
    profit = 0
    max = 0
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    for i in range(len(nums)-1,-1,-1):
        if(nums[i] > max):
            max = nums[i]
        else:
            profit += max-nums[i]
    print(profit)