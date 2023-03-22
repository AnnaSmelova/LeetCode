class Solution:
    def maxDepth(self, s: str) -> int:
        cnt = 0
        result = 0
        for i in s:
            if i == '(':
                cnt += 1
            elif i == ')':
                result = max(result, cnt)
                cnt -= 1
        return result
