class Solution:
    def ncr(self,r,c):
        res = 1
        for i in range(c):
            res*=r-i
            res/=i+1
        return int(res)
    def getRow(self, rowIndex: int) -> List[int]:
        ans=[]
        for i in range(1,rowIndex+2):
            ans.append(self.ncr(rowIndex, i-1))
        return ans