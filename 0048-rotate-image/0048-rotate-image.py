class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #optimal
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[0])):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(len(matrix)):
            matrix[i]=matrix[i][::-1]
        
        #bruteforce 
#         m=[]
#         for j in range(len(matrix[0])):
        
#             row=[]
#             for i in range(len(matrix)-1,-1,-1):
#                 row.append(matrix[i][j])
#             m.append(row)
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 matrix[i][j]=m[i][j]