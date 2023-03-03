class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if m == 0:
            return 0
        if m > n:
            return -1
        position = -1
        for i in range(n - m + 1):
            if position == -1 and haystack[i] == needle[0]:
                position = i
                for j in range(1,m):
                    if haystack[i + j] != needle[j]:
                        position = -1
                        break
                if position != -1:
                    return position
        return position
