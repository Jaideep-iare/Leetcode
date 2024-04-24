class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i,j=0,0
        g.sort()
        s.sort()
        content=0
        while i<len(g) and j<len(s):
            if g[i]<=s[j]:
                content+=1
                i+=1
            j+=1
        return content
            
