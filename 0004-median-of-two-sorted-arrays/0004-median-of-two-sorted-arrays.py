class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        k = n + m
        mid = k // 2
        if m < n:
            nums1, nums2 = nums2, nums1
            n, m = m, n

        left, right = 0, n - 1
        while True:
            i = (left + right) // 2
            j = mid - i - 2

            nums1_left = nums1[i] if i >= 0 else -float('inf')
            nums1_right = nums1[i + 1] if (i + 1) < n else float('inf')
            nums2_left = nums2[j] if j >= 0 else -float('inf')
            nums2_right = nums2[j + 1] if (j + 1) < m else float('inf')

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if k % 2:
                    return min(nums1_right, nums2_right)
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            elif nums1_left > nums2_right:
                right = i - 1
            else:
                left = i + 1
        