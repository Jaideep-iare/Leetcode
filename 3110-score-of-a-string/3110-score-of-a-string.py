class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        i = 0
        for elem in range(0, len(s) - 1):
            if (i < len(s)):
                sum += abs(ord(s[elem]) - ord(s[elem + 1]))
        return sum
            
            
        