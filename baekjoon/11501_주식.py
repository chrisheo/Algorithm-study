#https://www.acmicpc.net/problem/11501
import sys
testCases = int(sys.stdin.readline().rstrip("\n"))
for _ in range(testCases):
    n = int(sys.stdin.readline().rstrip("\n"))
    nums = list(map(int, sys.stdin.readline().rstrip("\n").split()))
    value=0
    max=0
    for i in range(len(nums)-1,-1,-1):
        if(nums[i] > max):
            max = nums[i]
        else:
            value+=max-nums[i]
    print(value)