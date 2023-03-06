class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binary_search(arr, target):
            if len(arr) == 1:
                return 0
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if mid > 0 and arr[mid - 1] < target <= arr[mid]:
                    return mid
                elif mid == 0 and arr[mid] >= target:
                    return mid
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid
        
        sub_longest = []
        for n in nums:
            if not sub_longest:
                sub_longest.append(n)
            else:
                if n > sub_longest[-1]:
                    sub_longest.append(n)
                else:
                    i = binary_search(sub_longest, n)
                    sub_longest[i] = n

        return len(sub_longest)
