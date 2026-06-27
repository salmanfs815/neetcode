# https://neetcode.io/problems/unionFind/question

# Union-Find (aka Disjoint Set) is a tool for finding disjoint sets of vertices in a graph or for cycle detection.
# Idea: iterate over graph's edges and union root parents of both vertices to make them part of the same connected component.
# Runtime is improved from O(n) for basic solution to ~ O(1) with union by rank (join smaller component into larger one) and path compression (make nodes in component direct children of root) optimizations.

# UnionFind class operations:
#   * UnionFind(int n) will initialize a disjoint set of size n.
#   * int find(int x) will return the root of the component that x belongs to.
#   * bool isSameComponent(int x, int y) will return whether x and y belong to the same component.
#   * bool union(int x, int y) will union the components that x and y belong to. If they are already in the same component, return false, otherwise return true.
#   * int getNumComponents() will return the number of components in the disjoint set.

class UnionFind:
    
    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}
        self.num_components = n
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootX] = rootY
            self.rank[rootY] += 1
        
        self.num_components -= 1
        return True

    def getNumComponents(self) -> int:
        return self.num_components
