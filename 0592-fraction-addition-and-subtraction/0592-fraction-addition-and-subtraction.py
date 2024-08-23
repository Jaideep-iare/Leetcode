import math
class Solution:
    def fractionAddition(self, expression: str) -> str:
        nres=0
        dres=1
        nr=dr=""
        slash_status=0
        for i in expression:
            if slash_status==0 and i!="/":
                nr+=i
            elif i=="/":
                slash_status=1
            elif slash_status==1 and i!="+" and i!="-":
                dr+=i
            else:
                nres = nres*int(dr)+dres*int(nr)
                dres = dres*int(dr)
                nr=""
                dr=""
                slash_status=0
                if i=="-":
                    nr+=i
        nres = nres*int(dr)+dres*int(nr)
        dres = dres*int(dr)
        gcd = math.gcd(nres,dres)
        nres//= gcd
        dres//=gcd
        if nres == 0:
            return "0/1"
        return str(nres)+"/"+str(dres)