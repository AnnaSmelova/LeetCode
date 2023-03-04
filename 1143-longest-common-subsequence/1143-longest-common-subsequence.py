class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        cache = [0] * n
        for l in text2:
            cnt = 0
            for i in range(n):
                if cnt < cache[i]:
                    cnt = cache[i]
                elif l == text1[i]:
                    cache[i] = cnt + 1
        return max(cache)
                    
        