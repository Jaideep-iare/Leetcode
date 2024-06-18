class Solution:
    def scoreOfString(self, s: str) -> int:
        val=0
        
        for i in range(0,len(s)-1):
            val+=abs(ord(s[i])-ord(s[i+1]))
            
        return val
            
            
        