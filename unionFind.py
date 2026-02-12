# https://neetcode.io/problems/unionFind/question

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
