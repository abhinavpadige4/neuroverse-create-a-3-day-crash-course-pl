# day2/14_review_sliding_window_fixed_variable_fas.py
"""Review: Sliding Window Techniques
===================================

This module contains concise, runnable examples that illustrate the most common
sliding‑window patterns used in array‑based interview problems.  Each function
focuses on a single pattern and includes a small ``if __name__ == "__main__"``
block that prints example input/output so the file can be executed directly.

Patterns covered
----------------
1. **Fixed‑size window** – the window length is known in advance (e.g. sum of
   ``k`` consecutive elements).
2. **Variable‑size window** – the window expands until a condition is broken
   and then contracts (e.g. longest subarray with sum ≤ ``k``).
3. **Fast & Slow pointers** – also known as the *two‑pointer* technique where
   one pointer moves ahead (fast) while the other lags (slow) to maintain a
   window.
4. **Opposite pointers** – pointers start at opposite ends and move towards
   each other (useful for problems like "minimum size subarray sum" when the
   array is sorted).

All examples run in ``O(n)`` time and ``O(1)`` extra space (apart from the
output list where required).
"""

from typing import List, Tuple

def fixed_size_window_sum(nums: List[int], k: int) -> List[int]:
    """Return the sum of every contiguous sub‑array of length ``k``.

    Example:
        >>> fixed_size_window_sum([1, 2, 3, 4, 5], 3)
        [6, 9, 12]
    """
    if k <= 0 or k > len(nums):
        return []
    window_sum = sum(nums[:k])
    result = [window_sum]
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        result.append(window_sum)
    return result


def longest_subarray_at_most_k(nums: List[int], limit: int) -> int:
    """Variable‑size window: longest sub‑array whose sum ≤ ``limit``.

    Returns the length of the longest valid window.
    """
    left = 0
    current_sum = 0
    max_len = 0
    for right, val in enumerate(nums):
        current_sum += val
        while current_sum > limit and left <= right:
            current_sum -= nums[left]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len


def min_subarray_len_with_sum_at_least(nums: List[int], target: int) -> int:
    """Fast & slow pointers: smallest length of a contiguous sub‑array with sum ≥ ``target``.

    If no such sub‑array exists, returns ``0``.
    """
    left = 0
    current_sum = 0
    min_len = float('inf')
    for right, val in enumerate(nums):
        current_sum += val
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1
    return 0 if min_len == float('inf') else min_len


def max_area_container(height: List[int]) -> int:
    """Opposite pointers: classic "Container With Most Water" problem.

    Two pointers start at the ends of the list and move towards each other,
    always discarding the shorter side because it cannot lead to a larger
    area.
    """
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        width = right - left
        area = width * min(height[left], height[right])
        max_area = max(max_area, area)
        # Move the pointer at the shorter line inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


if __name__ == "__main__":
    # Fixed‑size window demo
    print("Fixed‑size window sums (k=3):", fixed_size_window_sum([1, 2, 3, 4, 5], 3))

    # Variable‑size window demo
    arr = [2, 1, 5, 1, 3, 2]
    limit = 7
    print(f"Longest sub‑array with sum ≤ {limit}:", longest_subarray_at_most_k(arr, limit))

    # Fast & slow pointers demo
    target = 7
    print(f"Min length sub‑array with sum ≥ {target}:", min_subarray_len_with_sum_at_least(arr, target))

    # Opposite pointers demo
    heights = [1,8,6,2,5,4,8,3,7]
    print("Max water container area:", max_area_container(heights))
