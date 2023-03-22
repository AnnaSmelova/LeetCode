class Solution:
    def dfs(self, node, adj, visited):
            visited[node] = True
            if node not in adj:
                return
            for edge in adj[node]:
                self.path_min = min(self.path_min, edge[1])
                if not visited[edge[0]]:
                    self.dfs(edge[0], adj, visited)

    def minScore(self, n: int, roads: List[List[int]]) -> int: 
        self.path_min = float('inf')
        adj = {}
        for road in roads:
            adj.setdefault(road[0], []).append([road[1], road[2]])
            adj.setdefault(road[1], []).append([road[0], road[2]])
        
        visited = [False] * (n + 1)
        self.dfs(1, adj, visited)

        return self.path_min
