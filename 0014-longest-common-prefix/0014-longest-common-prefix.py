class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        s=0
        s1=strs[0]
        s2=strs[len(strs)-1]
        for i in range(len(s1)):
            if s1[i]==s2[i]:
                s+=1
            else:
                break
        return s1[0:s]
                    
            
                
                    
                    
                    