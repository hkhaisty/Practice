'''
Solution -- Recursive Depth First Search
Runtime Complexity -- O(m x n)
Space Complexity -- O(m x n)
'''
def num_islands(self, grid):
    def mark_landmass(grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]):
            return 
            
        if grid[row][col] == '1':
            grid[row][col] = '0'
            mark_landmass(grid, row - 1, col)
            mark_landmass(grid, row + 1, col)
            mark_landmass(grid, row, col - 1)
            mark_landmass(grid, row, col + 1)
        
    num_islands = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '1':
                num_islands += 1
                mark_landmass(grid, row, col)
                
    return num_islands
