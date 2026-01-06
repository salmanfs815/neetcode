# https://neetcode.io/problems/matrixBFS/question

# You are given a binary matrix, grid, where 0s represent land and 1s represent rocks that cannot be traversed.
# Return the length of the shortest path from the top-left corner of grid to the bottom-right corner such that all traversed cells are land cells. You may only move vertically and horizontally through land cells.
# If there is no such path, return -1.
# The length of a path is the number of moves from the starting cell to the ending cell.

# Example:
# Input: grid = [
#   [0, 0, 0, 0],
#   [1, 1, 0, 0],
#   [0, 0, 0, 1],
#   [0, 1, 0, 0]
# ]
# Output: 6

from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        visited.add((0,0))
        queue.append((0,0))
        length = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r == ROWS-1 and c == COLS-1:
                    return length
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr,dc in directions:
                    if min(r+dr, c+dc) >= 0 and r+dr < ROWS and c+dc < COLS and grid[r+dr][c+dc] == 0 and (r+dr, c+dc) not in visited:
                        visited.add((r+dr, c+dc))
                        queue.append((r+dr, c+dc))
            length += 1
        return -1
