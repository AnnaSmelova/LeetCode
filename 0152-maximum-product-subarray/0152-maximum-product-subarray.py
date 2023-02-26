class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max, current_min = 1, 1
        res = nums[0]
        
        for n in nums:
            vals = (n, n * current_max, n * current_min)
            current_max, current_min = max(vals), min(vals)
			
            res = max(res, current_max)
            
        return res
