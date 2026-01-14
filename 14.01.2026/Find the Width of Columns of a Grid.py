class Solution(object):
    def findColumnWidth(self, grid):

        if not grid or not grid[0]:
            return []

        res = []
        
        for j in range(len(grid[0])):   
            max_width= 0
            for i in range(len(grid)):   
                current_width = len(str(grid[i][j]))
                
                max_width = max(max_width, current_width)
            
            res.append(max_width)
            
        return res
