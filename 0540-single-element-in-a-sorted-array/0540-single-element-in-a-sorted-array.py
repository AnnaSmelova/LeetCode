class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, n
        while i < j:
            mid = (i + j) // 2
            if mid % 2 == 0:
                if mid > 0 and nums[mid] == nums[mid - 1]:
                    j = mid - 1
                elif mid < n - 1 and nums[mid] == nums[mid + 1]:
                    i = mid + 2
                else:
                    return nums[mid]
            else:
                if mid > 0 and nums[mid] == nums[mid - 1]:
                    i = mid + 1
                elif mid < n - 1 and nums[mid] == nums[mid + 1]:
                    j = mid
                else:
                    return nums[mid]
        return nums[i]
    