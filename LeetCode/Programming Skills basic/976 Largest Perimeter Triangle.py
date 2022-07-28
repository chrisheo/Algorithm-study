from calendar import c
from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        #가장 긴 변의 길이 < 나머지 두 변의 길이의 합, enumerate 사용법
        nums.sort(reverse=True)
        for i,x in enumerate(A[:-2]):
            if x < nums[ i + 1] + nums[ i + 2 ]:
                return x + nums[i+1] + nums[i+2]
        
        return 0
