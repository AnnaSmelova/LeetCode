from heapq import heappop, heappush


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        result = float('inf')
        heap = []  
        for n in set(nums):
            if n % 2 == 0:
                heappush(heap, (-1) * n)
            else:
                heappush(heap, (-2) * n)
        heap_min = (-1) * max(heap)
        while heap[0] % 2 == 0:
            heap_max = (-1) * heappop(heap)
            heappush(heap, (-1) * heap_max // 2)
            result = min(result, heap_max - heap_min)
            heap_min = min(heap_min, heap_max // 2)
        heap_max = (-1) * heappop(heap)
        result = min(result, heap_max - heap_min)
        return result


# TIME : O(N * LOG(N))
# SPACE : O(N)
        