from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        start = 1
        for i in nums:
            if i == 0:
                return 0
            elif i > 0:
                continue
            else:
                start = start * -1
        return start