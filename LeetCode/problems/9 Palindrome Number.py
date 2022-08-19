class Solution:
    def isPalindrome(self, x: int) -> bool:
        #우영우 구하기
        str_x = str(x)
        for i in range(len(x) / 2):
          if str_x[i] == str_x[-i - 1]:
            continue
          else:
            return False
        return True