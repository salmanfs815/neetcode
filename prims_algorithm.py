# https://neetcode.io/problems/prim

# Implement Prim's minimum spanning tree algorithm.

# A Minimum Spanning Tree (MST) is a tree that spans all the vertices in a given weighted, undirected graph while minimizing the total edge weight and avoiding cycles. It connects all nodes with exactly ∣V∣−1 edges, where V is the set of vertices, and has the lowest possible sum of edge weights.
# Prim's algorithm is a greedy algorithm that builds the MST of a graph starting from an arbitrary vertex. At each step, the algorithm adds the lightest edge connecting a vertex in the MST to a vertex outside the MST, effectively "growing" the MST one edge at a time.

# Objective: Given a weighted, undirected graph, find the minimum spanning tree (MST) using Prim's algorithm and return its total weight. If the graph is not connected, the total weight of the minimum spanning tree should be -1.

# Input:
#   * n - the number of vertices in the graph, where (2 <= n <= 100). Each vertex is labeled from 0 to n - 1.
#   * edges - a list of tuples, each representing an undirected edge in the form (u, v, w), where u and v are vertices connected by the edge, and w is the weight of the edge, where (1 <= w <= 10).

# Example
# Input: n = 5, edges = [[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5]]
# Output: 11

import heapq

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for a, b, w in edges:
            adj[a].append((b, w))
            adj[b].append((a, w))
        mstWeight = 0
        visit = set([0])
        minHeap = []
        for v, w in adj[0]:
            heapq.heappush(minHeap, (w, 0, v))
        while minHeap:
            weight, a, b = heapq.heappop(minHeap)
            if b not in visit:
                visit.add(b)
                mstWeight += weight
                for v, w in adj[b]:
                    if v not in visit:
                        heapq.heappush(minHeap, (w, b, v))
        return mstWeight if len(visit) == n else -1
