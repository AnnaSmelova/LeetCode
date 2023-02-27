class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        max_len = 0
        stack = deque()
        while end < len(s):
            if stack and s[end] in stack:
                max_len = max(max_len, len(stack))
                stack.popleft()
                start += 1
            else:
                stack.append(s[end])
                end += 1
        return max(max_len, len(stack))
        