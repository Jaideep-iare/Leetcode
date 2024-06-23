class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        alp="abcdefghijklmnopqrstuvwxyz"
        diff=0
        for i in range(len(s)):
            diff+=abs(s.index(s[i])-t.index(s[i]))
        return diff
        