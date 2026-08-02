class Solution(object):
    def romanToInt(self, s):
        romanNumber = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        for i in range(len(s) - 1):
            if romanNumber[s[i]] < romanNumber[s[i + 1]]:
                total -= romanNumber[s[i]]
            else:
                total += romanNumber[s[i]]

        total += romanNumber[s[-1]]
        return total