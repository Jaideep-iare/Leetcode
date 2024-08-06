class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        c=len(matrix[0])
        col0=1
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    if j!=0:
                        matrix[0][j]=0
                    else:
                        col0=0
        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][j]!=0:
                    if matrix[0][j]==0 or matrix[i][0]==0:
                        matrix[i][j]=0
        if matrix[0][0]==0:
            for j in range(c):
                matrix[0][j]=0
        if col0==0:
            for i in range(r):
                matrix[i][0]=0
        # r=len(matrix)
        # c=len(matrix[0])
        # row=[0]*r
        # col=[0]*c
        # for i in range(r):
        #     for j in range(c):
        #         if matrix[i][j]==0:
        #             row[i]=1
        #             col[j]=1
        # for i in range(r):
        #     for j in range(c):
        #         if row[i]==1 or col[j]==1:
        #             matrix[i][j]=0