class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #  function checks can we ship all weights with capacity <weight_for_check> within <days> days.
        def check_weight(weight_for_check: int) -> bool:
            days_cnt = 1
            current_weight = weight_for_check
            for weight in weights:
                if current_weight >= weight:
                    current_weight -= weight
                else:
                    days_cnt += 1
                    current_weight = weight_for_check - weight
            return days_cnt <= days

        #  we will use binary search
        #  left point - max weight in weights -> include
        #  right point - total weight + 1 -> exclude
        left, right = max(weights), sum(weights) + 1
        target_weight = float('inf')
        while left < right:
            mid = (left + right) // 2
            if check_weight(mid):
                target_weight = min(target_weight, mid)
                right = mid
            else:
                left = mid + 1
        return target_weight


# TIME : O(N * LOG(sum(weights) - max(weights)))
# SPACE : O(1)