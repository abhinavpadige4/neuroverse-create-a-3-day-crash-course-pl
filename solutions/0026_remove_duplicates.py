"""LeetCode 26. Remove Duplicates from Sorted Array
===================================================

**Problem statement**
Given a sorted integer array ``nums`` in non‑decreasing order, remove the duplicates **in‑place** such that each unique element appears only once. The relative order of the elements should be kept the same.

After removal, return the new length ``k`` of the array. The first ``k`` elements of ``nums`` must contain the unique values in sorted order. It does **not** matter what values exist beyond index ``k-1``.

**Constraints**
- ``1 <= nums.length <= 3 * 10⁴``
- ``-10⁴ <= nums[i] <= 10⁴``
- ``nums`` is sorted in non‑decreasing order.

**Solution overview**
The classic two‑pointer (slow‑fast) technique solves this in O(n) time and O(1) extra space.

- ``slow`` points to the last position of the *unique* part of the array.
- ``fast`` scans the array from left to right.
- When ``nums[fast]`` differs from ``nums[slow]`` we have found a new unique value; we increment ``slow`` and copy ``nums[fast]`` to ``nums[slow]``.
- At the end ``slow + 1`` is the length of the deduplicated array.

Because the input array is already sorted, equal values are contiguous, guaranteeing that the first time we see a different value it is the next unique element.

**Complexity analysis**
- Time: O(n) – each element is visited once.
- Space: O(1) – only a couple of integer variables are used.

**API**
The function follows the LeetCode signature:
```python
def removeDuplicates(nums: List[int]) -> int:
```
It mutates ``nums`` in‑place and returns the new length.
"""

from typing import List


def removeDuplicates(nums: List[int]) -> int:
    """Remove duplicates from a sorted list *in‑place*.

    Parameters
    ----------
    nums: List[int]
        A list of integers sorted in non‑decreasing order.

    Returns
    -------
    int
        The length ``k`` of the array after duplicates have been removed.
        The first ``k`` elements of ``nums`` contain the unique values.
    """
    if not nums:
        # Empty list – nothing to do
        return 0

    # ``slow`` is the index of the last unique element found.
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    # ``slow`` is zero‑based, so length is ``slow + 1``.
    return slow + 1


# ---------------------------------------------------------------------------
# Simple self‑test block – not executed on LeetCode but useful for local runs.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        ([1, 1, 2], [1, 2], 2),
        ([0,0,1,1,1,2,2,3,3,4], [0,1,2,3,4], 5),
        ([-1,0,0,0,3,3], [-1,0,3], 3),
        ([1], [1], 1),
        ([], [], 0),
    ]
    for arr, expected_vals, expected_len in test_cases:
        nums = list(arr)  # copy to avoid mutating the literal
        k = removeDuplicates(nums)
        assert k == expected_len, f"len mismatch: got {k}, expected {expected_len}"
        assert nums[:k] == expected_vals, f"array mismatch: got {nums[:k]}, expected {expected_vals}"
    print("All local tests passed.")
