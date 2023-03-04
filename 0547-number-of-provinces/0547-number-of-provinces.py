class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited= set()
        result = 0
        for i in range(len(isConnected)):
            if i not in visited:
                next_nodes_to_check = [i]
                while len(next_nodes_to_check):
                    current = next_nodes_to_check.pop()
                    if current not in visited:
                        visited.add(current)
                        next_nodes_to_check = [j for j,v in enumerate(isConnected[current]) if v and j not in visited] + next_nodes_to_check
                result += 1
        return result
    
