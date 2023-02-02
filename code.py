class Solution:
    def findBall(self, grid: List[List[int]]):
            nrows = len(grid)
            ncols = len(grid[0])
            def candrop(i,j):
                if i == nrows: return j # Ball falls out of bottom
                if j == ncols-1 and grid[i][j] == 1: return -1 # Ball hits right wall due to a l2r-leaning slat
                if j == 0 and grid[i][j] == -1: return -1 # Ball hits left wall due to a r2l-leaning slat
                if grid[i][j] == 1 and grid[i][j+1] == -1: return -1 # Ball lands in a V after rolling right
                if grid[i][j] == -1 and grid[i][j-1] == 1: return -1 # Ball lands in a V after rolling left
                return candrop(i+1,j+grid[i][j]) # No end case, continue by increasing y-coord by one and x-coord by 1 or -1 depending on roll direction.
            
            return [candrop(0,j) for j in range(ncols)]

        

