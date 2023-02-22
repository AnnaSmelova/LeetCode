class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #  function checks can we ship all weights with capacity <weight_for_check> within <days> days.
        def check_weight(weight_for_check: int) -> bool:
            days_cnt, current_weight = 0, 0
            for weight in weights:
                if current_weight + weight <= weight_for_check:
                    current_weight += weight
                else:
                    days_cnt += 1
                    current_weight = weight
            if current_weight > 0:
                days_cnt += 1
            return days_cnt <= days

        #  get total weight and max weight in weights
        weights_sum, weights_max = weights[0], weights[0]
        for i in range(1, len(weights)):
            weights_sum += weights[i]
            weights_max = max(weights_max, weights[i])

        #  we will use binary search
        #  left point - max weight in weights -> include
        #  right point - total weight + 1 -> exclude
        left, right = weights_max, weights_sum + 1
        target_weight = -1
        while left < right:
            mid = (left + right) // 2
            if check_weight(mid):
                target_weight = mid
                right = mid
            else:
                left = mid + 1
        return target_weight
    
# TIME : O(N * LOG(sum(weights) - max(weights))) 
# SPACE : O(1)
