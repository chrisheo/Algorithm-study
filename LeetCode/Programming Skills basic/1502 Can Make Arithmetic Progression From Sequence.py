from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = abs(arr[1] - arr[0])
        for i in range(len(arr) - 1):
            if abs(arr[i+1] - arr[i]) == diff:
                print(arr[i])
                continue
            else:
                return False
        return True
s = Solution()
s.canMakeArithmeticProgression([-68,-96,-12,-40,16])