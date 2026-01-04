# https://neetcode.io/problems/matrixDFS/history

# You are given a binary matrix, grid, where 0s represent land and 1s represent rocks that can not be traversed.
# Return the number of unique paths from the top-left corner of grid to the bottom-right corner such that all traversed cells are land cells. You may only move vertically or horizontally through land cells. For an individual unique path you cannot visit the same cell twice.

# Example:
# Input: grid = [
#   [0, 0, 0, 0],
#   [1, 1, 0, 0],
#   [0, 0, 0, 1],
# ]
# Output: 2

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c):
            if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visited or grid[r][c] == 1:
                return 0
            if r == ROWS-1 and c == COLS-1:
                return 1
            visited.add((r,c))
            count = 0
            count += dfs(r+1,c)
            count += dfs(r-1,c)
            count += dfs(r,c+1)
            count += dfs(r,c-1)
            visited.remove((r,c))
            return count
        return dfs(0,0)
        
