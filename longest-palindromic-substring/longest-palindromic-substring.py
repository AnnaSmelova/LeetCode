class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check_palindrome(s, l, r):
            while l >=0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        
        start, end = 0, 0
        for i in range(len(s)):
            lng_1 = check_palindrome(s, i, i)
            lng_2 = check_palindrome(s, i, i + 1)
            lng = max(lng_1, lng_2)

            if lng > end - start:
                start = i - (lng - 1) // 2
                end = i + lng // 2

        return s[start:end + 1]    
            