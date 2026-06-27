# https://neetcode.io/problems/dijkstra/question

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # adjacency list maps  {source: (destination, weight)}
        adj = {v: [] for v in range(n)}
        for s, d, w in edges:
            adj[s].append((d, w))
        
        # shortest maps {vertex: shortest_distance}
        shortest = {v: -1 for v in range(n)}

        # minHeap contains (shortest_distance, vertex)
        minHeap = [(0, src)]
        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if shortest[node] == -1:
                shortest[node] = weight
                for neighbor, edge in adj[node]:
                    if shortest[neighbor] == -1:
                        heapq.heappush(minHeap, (weight + edge, neighbor))
        return shortest
