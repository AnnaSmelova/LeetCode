class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(set)
        for u,v in connections:
            graph[u].add((v, True)) 
            graph[v].add((u, False))
        queue = deque([0])
        visited = set([0])
        change_edges = 0
        while queue:
            node = queue.popleft()
            for nei, is_in_connections in graph[node]:
                if nei not in visited:
                    change_edges += is_in_connections
                    queue.append(nei)
                    visited.add(nei)
        return change_edges
        