class Solution(object):
    def romanToInt(self, s):
        num = 0
        romans = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        i = 0
        while i < len(s):
            if i + 1 < len(s) and romans[s[i]] < romans[s[i + 1]]:
                num += romans[s[i + 1]] - romans[s[i]]
                i += 2
            else:
                num += romans[s[i]]
                i += 1
        return num

sol = Solution()
result = sol.romanToInt("MCMXCIV")
print(result)