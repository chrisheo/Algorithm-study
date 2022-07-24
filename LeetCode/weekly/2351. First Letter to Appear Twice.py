class Solution:
    def repeatedCharacter(self, s: str) -> str:
        output = ""
        dict_who_appeared = {}
        check_existence = False
        for i in range(len(s)):
            if (s[i] in dict_who_appeared):
                check_existence = True
            else:
                dict_who_appeared[s[i]] = i
            if (check_existence):
                output = s[i]
                return output
        return " "