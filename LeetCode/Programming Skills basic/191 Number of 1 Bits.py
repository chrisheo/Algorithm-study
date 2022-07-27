from itertools import count


class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).count('1')