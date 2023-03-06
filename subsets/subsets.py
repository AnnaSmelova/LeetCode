class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, current):
            result.append(current[:])
                
            for i in range(start, n):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()
    
        n = len(nums)
        result = []
        backtrack(0, [])
        return result


            
