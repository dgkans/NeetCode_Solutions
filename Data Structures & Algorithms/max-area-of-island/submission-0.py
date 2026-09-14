class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            #boundary conditions:
            if r < 0 or c < 0 or r > n_rows - 1 or c > n_cols -1:
                return 0
            #if its water/already traversed:
            if grid[r][c] == 0:
                return 0
            #if its land/mark 0:
            grid[r][c] = 0
            area = 1

            area += dfs(r+1,c)
            area += dfs(r-1,c)
            area += dfs(r, c+1)
            area += dfs(r, c-1)
            return area

        n_rows = len(grid)
        n_cols = len(grid[0])
        max_area = 0
        for m in range(n_rows):
            for n in range(n_cols):
                if grid[m][n] == 1:
                    area = dfs(m,n)
                    max_area = max(max_area,area)
        return max_area