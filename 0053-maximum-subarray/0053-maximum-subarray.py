class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_max = -float('inf')
        sum_cum = 0
        for n in nums:
            sum_cum += n
            if sum_max < sum_cum:
                sum_max = sum_cum
            if sum_cum < 0:
                sum_cum = 0
        return sum_max
