class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def divide_and_conquer(substr, k):
            if len(substr) < k:
                return 0
            d = Counter(substr)
            mid = -1
            for i, char in enumerate(substr):
                if d[char] < k:
                    mid = i
                    break
            if mid == -1:
                return len(substr)
            else:
                return max(divide_and_conquer(substr[:mid], k), divide_and_conquer(substr[mid + 1:], k))
        
        return divide_and_conquer(s, k)
                            