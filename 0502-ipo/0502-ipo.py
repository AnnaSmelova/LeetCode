from heapq import heappush, heappop


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        #  build tuples (project_capital, project_profit)
        #  sort it by min capital and min profit
        projects_info = sorted(list(zip(capital, profits)), key=lambda x: (x[0], x[1]))
        heap = []  # here we will use heap
        ind = 0
        for _ in range(k):
            while ind < len(projects_info) and projects_info[ind][0] <= w:
                #  push (-1)*profit, because we need pop max element, but heap returns min element
                heappush(heap, -projects_info[ind][1])
                ind += 1
            if not heap:
                break
            w += -heappop(heap)
        return w


# TIME : O(N * LOG(N))
# SPACE : O(N)
        