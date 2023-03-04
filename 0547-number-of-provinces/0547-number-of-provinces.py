class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        def dfs(node):
            for i, edge in enumerate(isConnected[node]):
                if edge and i not in visited:
                    visited.add(i)
                    dfs(i)
        
        result = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                result += 1
        return result
