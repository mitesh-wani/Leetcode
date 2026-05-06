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

# memorization method time:O(m*n*n) space:O(m*n*n)+O(m)
        # 3D array
        # dp=[[[-1 for _ in range(col)]for _ in range(col)]for _ in range(row)]
        # def maxPicker(i,j1,j2):
        #     # outside of the grid case
        #     if j1<0 or j2<0 or j1>col-1 or j2>col-1:return float('-inf')
        #     # last row return calculted output
        #     if i==row-1:
        #         if j1==j2:return grid[i][j1]
        #         else:return grid[i][j1]+grid[i][j2]
        #     #  both robots stay in the same cell, only one takes the cherries.
        #     if dp[i][j1][j2]!=-1:return dp[i][j1][j2]
        #     if j1==j2:grid_val=grid[i][j1]
        #     else: grid_val=grid[i][j1]+grid[i][j2]
        #     # 9 robo movement combination for robo1 and robo2 
        #     x=[-1]*9
        #     x[0]=maxPicker(i+1,j1-1,j2-1) # down_left,down_left
        #     x[1]=maxPicker(i+1,j1-1,j2)     # down_left,down
        #     x[2]=maxPicker(i+1,j1-1,j2+1)   # down_left,down_right
        #     x[3]=maxPicker(i+1,j1,j2-1)     # down,down_left
        #     x[4]=maxPicker(i+1,j1,j2)       # down,down
        #     x[5]=maxPicker(i+1,j1,j2+1)     # down,down_right
        #     x[6]=maxPicker(i+1,j1+1,j2-1)   # down_right.down_left
        #     x[7]=maxPicker(i+1,j1+1,j2)     # down_right,down
        #     x[8]=maxPicker(i+1,j1+1,j2+1)   # down_right,down_left
        #     dp[i][j1][j2]= grid_val+max(x)
        #     return dp[i][j1][j2]
        # return maxPicker(0,0,col-1)

# tabulation method time:O(m*n*n) space:O(m*n*n)
        # dp=[[[-1 for _ in range(col)]for _ in range(col)]for _ in range(row)]
        # for i in range(row-1,-1,-1):
        #     for j1 in range(col):
        #         for j2 in range(col):
        #             if i==row-1:
        #                 if j1==j2:dp[i][j1][j2]=grid[i][j1]
        #                 else:dp[i][j1][j2]=grid[i][j1]+grid[i][j2]
        #             else:
        #                 if j1==j2:grid_val=grid[i][j1]
        #                 else:grid_val= grid[i][j1]+grid[i][j2]
        #                 # this used for index out of range error
        #                 def helper(r, c1, c2):
        #                     if 0 <= c1 < col and 0 <= c2 < col:
        #                         return dp[r][c1][c2]
        #                     return -float('inf')
        #                 x=[-float('inf')]*9
        #                 x[0]=helper(i+1,j1-1,j2-1) 
        #                 x[1]=helper(i+1,j1-1,j2)
        #                 x[2]=helper(i+1,j1-1,j2+1)
        #                 x[3]=helper(i+1,j1,j2-1)
        #                 x[4]=helper(i+1,j1,j2)
        #                 x[5]=helper(i+1,j1,j2+1)
        #                 x[6]=helper(i+1,j1+1,j2-1)
        #                 x[7]=helper(i+1,j1+1,j2)
        #                 x[8]=helper(i+1,j1+1,j2+1)
        #                 dp[i][j1][j2]= grid_val+max(x)
        # return dp[0][0][col-1]

# tabulation method time:O(m*n*n) space:O(m*n*n)
        prev=[[-float('inf')]*col for _ in range(col)]
        # curr replace with dp[i]
        # prev replace wih dp[i+1]
        for i in range(row-1,-1,-1):
            curr=[[-float('inf')]*col for _ in range(col)]
            for j1 in range(col):
                for j2 in range(col):
                    if i==row-1:
                        if j1==j2:curr[j1][j2]=grid[i][j1]
                        else:curr[j1][j2]=grid[i][j1]+grid[i][j2]
                    else:
                        if j1==j2:grid_val=grid[i][j1]
                        else:grid_val= grid[i][j1]+grid[i][j2]
                        # this used for index out of range error
                        def helper(r, c1, c2):
                            if 0 <= c1 < col and 0 <= c2 < col:
                                return prev[c1][c2]
                            return -float('inf')
                        x=[-float('inf')]*9
                        x[0]=helper(i+1,j1-1,j2-1) 
                        x[1]=helper(i+1,j1-1,j2)
                        x[2]=helper(i+1,j1-1,j2+1)
                        x[3]=helper(i+1,j1,j2-1)
                        x[4]=helper(i+1,j1,j2)
                        x[5]=helper(i+1,j1,j2+1)
                        x[6]=helper(i+1,j1+1,j2-1)
                        x[7]=helper(i+1,j1+1,j2)
                        x[8]=helper(i+1,j1+1,j2+1)
                        curr[j1][j2]= grid_val+max(x)
            prev=curr
        return prev[0][col-1]
                       



    


