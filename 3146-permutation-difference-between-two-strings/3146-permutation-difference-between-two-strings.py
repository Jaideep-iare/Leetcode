class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        alp={}
        diff=0
        for i in range(len(s)):
            if s.index(s[i]) not in alp:
                diff+=abs(s.index(s[i])-t.index(s[i]))
                alp[s[i]]=t.index(s[i])
            else:
                diff+=abs(s.index(s[i])-alp[s[i]])
        return diff
        