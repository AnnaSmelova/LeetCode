"""
1011. Capacity To Ship Packages Within D Days

A conveyor belt has packages that must be shipped from one port to another within <days> days.
The ith package on the conveyor belt has a weight of weights[i].
Each day, we load the ship with packages on the conveyor belt (in the order given by weights).
We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being
shipped within <days> days.

Example 1:
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10
Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the
packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

Example 2:
Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4

Example 3:
Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1

Constraints:
1 <= days <= weights.length <= 5 * 104
1 <= weights[i] <= 500
"""
import unittest
from typing import List


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


class CustomCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    #  from example 1
    def test_case_1(self):
        weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        days = 5
        result_expected = 15
        result = self.solution.shipWithinDays(weights, days)
        self.assertEqual(result, result_expected)

    #  from example 2
    def test_case_2(self):
        weights = [3, 2, 2, 4, 1, 4]
        days = 3
        result_expected = 6
        result = self.solution.shipWithinDays(weights, days)
        self.assertEqual(result, result_expected)

    #  from example 3
    def test_case_3(self):
        weights = [1, 2, 3, 1, 1]
        days = 4
        result_expected = 3
        result = self.solution.shipWithinDays(weights, days)
        self.assertEqual(result, result_expected)

    #  one weight - one day
    def test_case_4(self):
        weights = [6]
        days = 1
        result_expected = 6
        result = self.solution.shipWithinDays(weights, days)
        self.assertEqual(result, result_expected)

    #  two weights - two days
    def test_case_5(self):
        weights = [1, 2]
        days = 2
        result_expected = 2
        result = self.solution.shipWithinDays(weights, days)
        self.assertEqual(result, result_expected)

    #  two weights - one day
    def test_case_6(self):
        weights = [1, 2]
        days = 1
        result_expected = 3
        result = self.solution.shipWithinDays(weights, days)
        self.assertEqual(result, result_expected)


unittest.main()
