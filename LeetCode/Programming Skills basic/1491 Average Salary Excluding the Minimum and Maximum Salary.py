from numpy import average


class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        return average(salary[1:-1])