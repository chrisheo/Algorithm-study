class Solution(object):
    def areAlmostEqual(self, s1, s2):
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                count+=1
        if (count==2 or count==0) and sorted(s1)==sorted(s2):
            return True
        return False

s = Solution()
print(s.areAlmostEqual("kelb", "kbel"))