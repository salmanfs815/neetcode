# https://neetcode.io/problems/kruskal

# Kruskal's Minimum Spanning Tree Algorithm

# A Minimum Spanning Tree (MST) is a tree that spans all the vertices in a given weighted, undirected graph while minimizing the total edge weight and avoiding cycles. It connects all nodes with exactly ∣V∣−1 edges, where V is the set of vertices, and has the lowest possible sum of edge weights.
# Kruskal's algorithm is a greedy algorithm that finds the MST of a weighted, undirected graph. It sorts all the edges from least weight to greatest, and iteratively adds edges to the MST, ensuring that each new edge doesn't form a cycle.

# Input:
#   * n - the number of vertices in the graph, where (2 <= n <= 100). Each vertex is labeled from 0 to n - 1.
#   * edges - a list of tuples, each representing an undirected edge in the form (u, v, w), where u and v are vertices connected by the edge, and w is the weight of the edge, where (1 <= w <= 10).

# Output:
#   * total weight of MST for connected graph, otherwise -1

import heapq
from union_find import UnionFind

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minHeap = []
        for a, b, w in edges:
            heapq.heappush(minHeap, (w, a, b))
        unionFind = UnionFind(n)
        mst = []
        mstWeight = 0
        while len(mst) < n-1 and minHeap:
            w, a, b = heapq.heappop(minHeap)
            if unionFind.union(a, b):
                mst.append([a, b])
                mstWeight += w
        return mstWeight if len(mst) == n-1 else -1
