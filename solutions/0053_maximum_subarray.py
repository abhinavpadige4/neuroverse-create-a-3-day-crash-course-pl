"""LeetCode 53 - Maximum Subarray
=================================

Problem statement
-----------------
Given an integer array ``nums`` find the contiguous subarray (containing at least one
number) which has the largest sum and return its sum.

Typical solution
----------------
Kadane's algorithm solves the problem in O(n) time and O(1) extra space.
We keep two variables while iterating:

* ``current`` – the maximum sum of a subarray ending at the current index.
  It is either the current element alone (start a new subarray) or the previous
  ``current`` plus the current element.
* ``best`` – the maximum sum seen so far across all positions.

Whenever ``current`` becomes negative we reset it to the current element – this
is equivalent to "dropping" the previous subarray because extending it would only
decrease the sum.

The function returns ``best`` after processing the whole list.

Complexity
----------
* Time: O(n) – single pass through the array.
* Space: O(1) – only a few integer variables.
"""

from typing import List


def max_subarray(nums: List[int]) -> int:
    """Return the maximum possible sum of a contiguous subarray.

    Parameters
    ----------
    nums: List[int]
        The input list of integers (may contain negative numbers).

    Returns
    -------
    int
        The largest sum of any contiguous subarray.
    """
    if not nums:
        raise ValueError("Input list 'nums' must contain at least one element")

    # Initialise both trackers with the first element.
    current = best = nums[0]

    # Iterate from the second element onward.
    for num in nums[1:]:
        # Either extend the previous subarray or start a new one at `num`.
        current = max(num, current + num)
        # Update the global best if the new current is larger.
        best = max(best, current)

    return best


# Simple sanity test when the module is executed directly.
if __name__ == "__main__":
    test_cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),  # classic example
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
        ([-1, -2, -3, -4], -1),  # all negatives -> largest (least negative) element
    ]
    for arr, expected in test_cases:
        result = max_subarray(arr)
        assert result == expected, f"Failed for {arr}: expected {expected}, got {result}"
    print("All quick tests passed.")
