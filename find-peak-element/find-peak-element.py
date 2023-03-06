class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def bin_search(nums, left, right):
            if left == right:
                return left
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return bin_search(nums, left, mid)
            return bin_search(nums, mid + 1, right)

        return bin_search(nums, 0, len(nums) - 1)
        