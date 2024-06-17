class Solution:
    def isValid(self, s: str) -> bool:
        d={'(':1,")":-1,"[":2,"]":-2,"{":3,"}":-3}
        l=[]
        top=0
        for i in s:
            if top+d[i]==0 and top>0:
                l.pop()
                if len(l)>0:
                    top=l[-1]
                else:
                    top=0
            else:
                l.append(d[i])
                top=d[i]
        print(l)
        if len(l)==0:
            return True
        return False
            
            
                
            
            
            