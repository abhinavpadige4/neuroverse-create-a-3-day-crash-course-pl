# -*- coding: utf-8 -*-
"""day1/01_review_arrays_hash_maps_two_sum_pattern_.py

Review module for Day 1 of the 3‑day crash plan.
It covers the fundamental concepts that appear in almost every array‑based
LeetCode interview problem:

* Basic list operations and slicing
* Hash‑map (dict) usage for O(1) look‑ups
* The classic *Two‑Sum* pattern – finding a pair that satisfies a target
* Prefix‑sum technique – turning range‑sum queries into O(1) look‑ups after O(n)
  preprocessing

The file is deliberately self‑contained: it can be executed directly to see
example runs and printed explanations.  All helper functions are also imported
by the concrete solution files under ``solutions/``.
"""

from __future__ import annotations

from typing import List, Tuple, Dict

# ---------------------------------------------------------------------------
# 1. Basic array (list) utilities
# ---------------------------------------------------------------------------

def rotate_left(arr: List[int], k: int) -> List[int]:
    """Return a new list rotated *k* steps to the left.

    Example:
        >>> rotate_left([1, 2, 3, 4, 5], 2)
        [3, 4, 5, 1, 2]
    """
    n = len(arr)
    if n == 0:
        return []
    k %= n
    return arr[k:] + arr[:k]


def reverse_in_place(arr: List[int]) -> None:
    """Reverse a list *in place* (mutates the original list).

    Example:
        >>> a = [1, 2, 3]
        >>> reverse_in_place(a)
        >>> a
        [3, 2, 1]
    """
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

# ---------------------------------------------------------------------------
# 2. Two‑Sum pattern (hash‑map single pass)
# ---------------------------------------------------------------------------

def two_sum(nums: List[int], target: int) -> Tuple[int, int] | None:
    """Return the *indices* of the two numbers that add up to ``target``.

    The implementation follows the classic interview pattern:
    * Iterate once over ``nums``.
    * For each value ``x`` compute ``complement = target - x``.
    * If ``complement`` is already in the hash‑map we have found the answer.
    * Otherwise store ``x`` with its index for future look‑ups.

    Time   : O(n)
    Space  : O(n) for the auxiliary dictionary.

    Returns ``None`` when no such pair exists.
    """
    lookup: Dict[int, int] = {}
    for i, x in enumerate(nums):
        complement = target - x
        if complement in lookup:
            return lookup[complement], i
        lookup[x] = i
    return None

# ---------------------------------------------------------------------------
# 3. Prefix‑sum technique
# ---------------------------------------------------------------------------

def prefix_sums(arr: List[int]) -> List[int]:
    """Return the prefix‑sum array of ``arr``.

    ``prefix[i]`` holds the sum of ``arr[0]`` … ``arr[i]`` (inclusive).
    This enables O(1) range‑sum queries:
        sum(arr[l:r+1]) == prefix[r] - prefix[l-1]   (with l > 0)
    """
    pref: List[int] = []
    running = 0
    for num in arr:
        running += num
        pref.append(running)
    return pref


def range_sum(pref: List[int], left: int, right: int) -> int:
    """Compute the sum of ``arr[left:right+1]`` using a pre‑computed prefix array.

    ``pref`` must be the result of ``prefix_sums`` on the original array.
    """
    if left == 0:
        return pref[right]
    return pref[right] - pref[left - 1]

# ---------------------------------------------------------------------------
# 4. Demonstration when the module is run directly
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # 1. Basic array ops
    print("--- Basic array utilities ---")
    original = [1, 2, 3, 4, 5]
    print("original:", original)
    print("rotate left by 2:", rotate_left(original, 2))
    rev = original.copy()
    reverse_in_place(rev)
    print("reversed in place:", rev)

    # 2. Two‑Sum pattern
    print("\n--- Two‑Sum pattern ---")
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"nums={nums}, target={target} => indices {result}")

    # 3. Prefix‑sum usage
    print("\n--- Prefix‑sum technique ---")
    arr = [3, 1, 4, 1, 5, 9, 2]
    pref = prefix_sums(arr)
    print("array:", arr)
    print("prefix sums:", pref)
    l, r = 2, 5
    print(f"sum(arr[{l}:{r}] ) =", range_sum(pref, l, r))
