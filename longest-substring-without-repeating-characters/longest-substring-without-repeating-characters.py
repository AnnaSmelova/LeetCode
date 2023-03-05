class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        end = 0
        max_len = 0
        stack = deque()
        while end < len(s):
            if stack and s[end] in stack:
                max_len = max(max_len, len(stack))
                stack.popleft()
            else:
                stack.append(s[end])
                end += 1
        return max(max_len, len(stack))
        