class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        #각 숫자의 합과 곱의 차
        sum = 0
        product = 1
        str_n = str(n)
        for i in range(len(str_n)):
            sum += int(str_n[i])
            product *= int(str_n[i])
        return product - sum           