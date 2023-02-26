class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        lng_1, lng_2 = len(word1), len(word2)
        if lng_1 == 0 or lng_2 == 0:
            return lng_1 + lng_2

        dp = [[0] * (lng_2 + 1) for _ in range(lng_1 + 1)]

        for i in range(1, lng_1 + 1):
            dp[i][0] = i
        for j in range(1, lng_2 + 1):
            dp[0][j] = j

        for i in range(1, lng_1 + 1):
            for j in range(1, lng_2 + 1):
                lng_change = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    lng_change += 1
                lng_del = dp[i][j - 1] + 1
                lng_insert = dp[i - 1][j] + 1

                dp[i][j] = min(lng_change, lng_del, lng_insert)

        return dp[lng_1][lng_2]


# TIME : O(len(word1) * len(word2))
# SPACE : O(len(word1) * len(word2))


