class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, current):
            if len(current) == k:  
                result.append(current[:])
                return
            for i in range(start, n):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()
        
        result = []
        n = len(nums)
        for k in range(n + 1):
            backtrack(0, [])
        return result
