class Solution:
    def numb(self,r,c):
        
        res=1
        for i in range(c):
            res *= r-i
            res /= i+1
        return int(res)
        
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        
        for i in range(1,numRows+1):
            x=[]
            for j in range(1,i+1):
                x.append(self.numb(i-1,j-1))
            ans.append(x)
        return ans