class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        """
        m,n=len(matrix),len(matrix[0])
        # any zero found in 1s row and 1st colum if fountd then true
        #/* Flag if there is any zero in first row */
        firstRow = -1           
        # /* Flag if there is any zero in first column */
        firstColumn = -1 
        for a in matrix[0]:
            if a==0:
                firstRow=0
        for j in range(m):
            if matrix[j][0]==0:
                firstColumn=0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        # for i in range(m):
        #     for j in range(1,n):
        #         if matrix[i][j]==0:
        #             matrix[0][j]=0
        
        for i in range(1,m):
            if matrix[i][0]==0:
                matrix[i]=[0]*n
            
        for j in range(n):
            if matrix[0][j]==0:
                for i in range(1,m):
                    matrix[i][j]=0
        if firstRow == 0:
            matrix[0] = [0] * n
            
        if firstColumn == 0:
            for i in range(m):
                matrix[i][0] = 0
        print(matrix)

        return matrix