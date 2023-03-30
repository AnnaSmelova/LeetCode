class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        def dp(index, time):
            if index > len(satisfaction) -1: 
                return 0 
            if (index, time) in memo: 
                return memo[(index, time)]
            memo[(index, time)] = max(satisfaction[index]*time + dp(index +1, time +1), dp(index + 1, time))
            return memo[(index, time)]
        memo = {} 
        return dp(0,1)
        