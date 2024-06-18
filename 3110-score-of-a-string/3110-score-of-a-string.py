class Solution:
    def scoreOfString(self, s: str) -> int:
        val=0
        n=len(s)
        for i in range(1,n,2):
            if i!=n-1:
                val+=abs(ord(s[i-1])-ord(s[i]))+abs(ord(s[i+1])-ord(s[i]))
            else:
                val+=abs(ord(s[i-1])-ord(s[i]))
        return val
            
            
        