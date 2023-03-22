class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        i, j = 0, 0
        n = len(nums)
        d = {}
        while j < n:
            diff_current = nums[j] - nums[i]
            if diff_current == diff:
                if i in d.keys():
                    d[i] = 1
                d[j] = 0
                j += 1
            elif diff_current < diff:
                j += 1
            else:
                i += 1
        return sum(d.values())
        