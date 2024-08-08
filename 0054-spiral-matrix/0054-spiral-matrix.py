class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l=0
        r=len(matrix[0])-1
        t=0
        b=len(matrix)-1 
        x=[]
        while l<=r and t<=b:
            #left to right
            for i in range(l,r+1):
                x.append(matrix[t][i])
            t+=1
            #top to bottom
            for i in range(t,b+1):
                x.append(matrix[i][r])
            r-=1
            #right to left
            if t<=b:
                for i in range(r,l-1,-1):
                    x.append(matrix[b][i])
                b-=1
            #bottom to top
            if l<=r:
                for i in range(b,t-1,-1):
                    x.append(matrix[i][l])
                l+=1
        return x
        