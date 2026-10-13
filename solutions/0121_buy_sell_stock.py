"""
LeetCode 121 - Best Time to Buy and Sell Stock (Easy)
======================================================
Problem:
    Given an array prices where prices[i] is the price of a given stock on the i-th day,
    find the maximum profit you can achieve from a single transaction.
    You must buy before you sell. If no profit is possible, return 0.

Approach:
    Single pass - track the minimum price seen so far and the maximum profit.
    For each day, we either:
      - Buy at the current price (if it's lower than our min so far)
      - Sell at the current price (calculate profit = current price - min price)

    Time Complexity: O(n)
    Space Complexity: O(1)
"""


class Solution:
    def maxProfit(self, prices):
        """
        Calculate the maximum profit from a single buy-sell transaction.

        Args:
            prices: List[int] - Array of stock prices where prices[i] is the price on day i.

        Returns:
            int - Maximum profit achievable, or 0 if no profit is possible.
        """
        if not prices or len(prices) < 2:
            return 0

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # Update minimum price seen so far
            min_price = min(min_price, price)
            # Calculate profit if we sell today
            profit = price - min_price
            # Update maximum profit
            max_profit = max(max_profit, profit)

        return max_profit


# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()

    # Test 1: Standard case - buy at 1, sell at 5
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5, "Test 1 failed"

    # Test 2: Prices only decrease - no profit possible
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0, "Test 2 failed"

    # Test 3: Single element
    assert sol.maxProfit([1]) == 0, "Test 3 failed"

    # Test 4: Empty array
    assert sol.maxProfit([]) == 0, "Test 4 failed"

    # Test 5: Two elements, profit possible
    assert sol.maxProfit([2, 3]) == 1, "Test 5 failed"

    # Test 6: Two elements, no profit
    assert sol.maxProfit([3, 2]) == 0, "Test 6 failed"

    # Test 7: All same prices
    assert sol.maxProfit([5, 5, 5, 5]) == 0, "Test 7 failed"

    # Test 8: Profit at the end
    assert sol.maxProfit([1, 2, 3, 4, 5]) == 4, "Test 8 failed"

    # Test 9: Large values
    assert sol.maxProfit([100000, 1, 100000]) == 99999, "Test 9 failed"

    # Test 10: Negative prices (edge case)
    assert sol.maxProfit([-5, -3, -1]) == 4, "Test 10 failed"

    print("All tests passed!")
