# https://neetcode.io/problems/topologicalSort/

# Topological sort is an algorithm for linearly ordering the vertices of a directed acyclic graph such that for every directed edge (u,v), vertex u comes before v in the ordering.
# Note: There may be multiple valid topological sorts for a given graph.

# Input:
#   * n - the number of vertices in the graph (labeled from 0 to n-1).
#   * edges - a list of pairs, each representing a directed edge in the form (u, v), where u is the source vertex and v is the destination vertex.

# Output:
#   * list of vertices representing a valid topological ordering; empty list if graph contains cycle

# Example 1:
#   * Input: n = 6, edges = [[2,3], [3,1], [4,0], [4,1], [5,0], [5,2]]
#   * Output: [5, 4, 2, 3, 1, 0]

# Example 2:
#   * Input: n = 3, edges = [[0,1], [1,2], [2,0]]
#   * Output: []

class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(i):
            if i in path:
                return False
            if i in visit:
                return True
            visit.add(i)
            path.add(i)
            for neighbour in adj[i]:
                if not dfs(neighbour):
                    return False
            path.remove(i)
            topSort.append(i)
            return True
            
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
        topSort = []
        visit = set()
        path = set()
        for i in range(n):
            if not dfs(i):
                return []
        return topSort[::-1]
