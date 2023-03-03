class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        product_largest = -float('inf')
        product_min, product_max = 1, 1
        for n in nums:
            p_current = (n, n * product_min, n * product_max)
            product_min = min(p_current)
            product_max = max(p_current)
            product_largest = max(product_largest, product_max)
        return product_largest
