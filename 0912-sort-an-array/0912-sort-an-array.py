class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Counting sort
        counts = {} 
        min_val, max_val = float('inf'), -float(inf)
        for val in nums:
            counts[val] = counts.get(val, 0) + 1
            min_val = min(min_val, val)
            max_val = max(max_val, val)

        index = 0
        for val in range(min_val, max_val + 1, 1):
            while counts.get(val, 0) > 0:
                nums[index] = val
                index += 1
                counts[val] -= 1
        return nums
