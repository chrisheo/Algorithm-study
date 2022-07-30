
class Solution:
    def isHappy(self, n):
        seen = set()
        while n not in seen:
            #본건 기억하면 된다.
            seen.add(n)
            n = sum([int(x) **2 for x in str(n)])
        return n == 1



