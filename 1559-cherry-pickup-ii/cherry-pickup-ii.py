class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        row=len(grid) # m
        col=len(grid[0]) # n
        # recursive time:O(9^m) space:O(m)
        # def maxPicker(i,j1,j2):
        #     # outside of the grid case
        #     if j1<0 or j2<0 or j1>col-1 or j2>col-1:return float('-inf')
        #     # last row return calculted output
        #     if i==row-1:
        #         if j1==j2:return grid[i][j1]
        #         else:return grid[i][j1]+grid[i][j2]
        #     #  both robots stay in the same cell, only one takes the cherries.
        #     if j1==j2:grid_val=grid[i][j1]
        #     else: grid_val=grid[i][j1]+grid[i][j2]

        #     x=[-1]*9
        #     x[0]=maxPicker(i+1,j1-1,j2-1) 
        #     x[1]=maxPicker(i+1,j1-1,j2)
        #     x[2]=maxPicker(i+1,j1-1,j2+1)
        #     x[3]=maxPicker(i+1,j1,j2-1)
        #     x[4]=maxPicker(i+1,j1,j2)
        #     x[5]=maxPicker(i+1,j1,j2+1)
        #     x[6]=maxPicker(i+1,j1+1,j2-1)
        #     x[7]=maxPicker(i+1,j1+1,j2)
        #     x[8]=maxPicker(i+1,j1+1,j2+1)

        #     return grid_val+max(x)
        # return maxPicker(0,0,col-1)

        # memorization method time:O(m*m) space:O(m*n*n)
        # 3D array
        dp=[[[-1 for _ in range(col)]for _ in range(col)]for _ in range(row)]
        def maxPicker(i,j1,j2):
            # outside of the grid case
            if j1<0 or j2<0 or j1>col-1 or j2>col-1:return float('-inf')
            # last row return calculted output
            if i==row-1:
                if j1==j2:return grid[i][j1]
                else:return grid[i][j1]+grid[i][j2]
            #  both robots stay in the same cell, only one takes the cherries.
            if dp[i][j1][j2]!=-1:return dp[i][j1][j2]
            if j1==j2:grid_val=grid[i][j1]
            else: grid_val=grid[i][j1]+grid[i][j2]
            # 9 robo movement combination for robo1 and robo2 
            x=[-1]*9
            x[0]=maxPicker(i+1,j1-1,j2-1) # down_left,down_left
            x[1]=maxPicker(i+1,j1-1,j2)     # down_left,down
            x[2]=maxPicker(i+1,j1-1,j2+1)   # down_left,down_right
            x[3]=maxPicker(i+1,j1,j2-1)     # down,down_left
            x[4]=maxPicker(i+1,j1,j2)       # down,down
            x[5]=maxPicker(i+1,j1,j2+1)     # down,down_right
            x[6]=maxPicker(i+1,j1+1,j2-1)   # down_right.down_left
            x[7]=maxPicker(i+1,j1+1,j2)     # down_right,down
            x[8]=maxPicker(i+1,j1+1,j2+1)   # down_right,down_left
            dp[i][j1][j2]= grid_val+max(x)
            return dp[i][j1][j2]
        return maxPicker(0,0,col-1)

        