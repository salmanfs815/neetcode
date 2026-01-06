# https://neetcode.io/problems/graph/question

# Directed graph class using HashMap/dict as adjacency list

# Contraints:
# - Each vertex value will be a unique integer.
# - Multiple edges from one vertex to another are not allowed.
# - A vertex will not have an edge to itself, but the graph may contain a cycle.
# - The graph is not necessarily connected (there may be disconnected components).

class Graph:
    
    # initialize an empty directed graph
    def __init__(self):
        self.graph = {}

    # add an edge from src to dst if it does not already exist
    # if either src or dst do not exist, add them to the graph
    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = []
        if dst not in self.graph:
            self.graph[dst] = []
        self.graph[src].append(dst)

    # will remove the edge from src to dst if it exists
    # return whether the edge was removed
    # either src or dst may not exist in the graph
    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph or dst not in self.graph:
            return False
        self.graph[src].remove(dst)
        return True

    # will return whether there is a path from src to dst
    # assume both src and dst exist in the graph
    # BFS
    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        queue = deque()
        visited.add(src)
        queue.append(src)
        while queue:
            node = queue.popleft()
            if node == dst:
                return True
            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        return False
