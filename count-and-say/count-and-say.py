class Solution:
    def countAndSay(self, n: int) -> str:
        def count(s):
            num = 1
            res = ''
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    num += 1
                else:
                    res += str(num) + s[i - 1]
                    num = 1
            res += str(num) + s[len(s) - 1]
            return res
            
        dp = [''] * (n + 1)
        dp[1] = '1'
        for j in range(2, n + 1):
            dp[j] = count(dp[j - 1])
        
        return dp[n]
        
        