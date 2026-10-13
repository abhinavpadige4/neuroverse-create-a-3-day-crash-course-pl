'''\
LeetCode 53 – Maximum Subarray
--------------------------------
Problem statement
-----------------
Given an integer array ``nums`` find the contiguous sub‑array (containing at least one
number) which has the largest sum and return its sum.

Typical interview pattern
--------------------------
* **Kadane's algorithm** – keep a running sum of the current sub‑array. If the sum
  becomes negative we discard it because extending it would only make future sums
  smaller. Simultaneously track the best sum seen so far.
* One‑pass, O(n) time, O(1) extra space.

Recap / notes
-------------
* ``current`` – sum of the sub‑array that ends at the current index.
* ``best`` – maximum of all ``current`` values observed.
* Update rule::

    current = max(num, current + num)
    best    = max(best, current)

* The ``max(num, ...)`` part decides whether to start a new sub‑array at the current
  element or to extend the previous one.
* Edge cases handled automatically: all negative numbers (the largest single
  element is returned) and single‑element arrays.

Complexity
----------
* **Time:** O(n) – one linear scan.
* **Space:** O(1) – only a few integer variables.

Implementation
--------------
The function ``max_subarray`` follows the description above and is deliberately
kept simple for readability in an interview setting.
'''\

def max_subarray(nums):
    """Return the maximum sum of a contiguous sub‑array.

    Parameters
    ----------
    nums : List[int]
        List of integers (can be positive, negative or zero).

    Returns
    -------
    int
        The maximum possible sum of any contiguous sub‑array.
    """
    if not nums:
        raise ValueError("Input list 'nums' must contain at least one element")

    # Initialise both trackers with the first element so that all‑negative arrays work.
    current = best = nums[0]
    for num in nums[1:]:
        # Either extend the previous sub‑array or start a new one at 'num'.
        current = max(num, current + num)
        best = max(best, current)
    return best

# Simple sanity‑check tests that can be run directly.
if __name__ == "__main__":
    test_cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),   # classic example, sub‑array [4,-1,2,1]
        ([1], 1),                               # single element
        ([-1, -2, -3, -4], -1),                  # all negatives
        ([5, 4, -1, 7, 8], 23),                  # whole array is best
        ([0, -3, 5, -2, 1, 2, -1, 2, -3, 4], 9) # mixed values
    ]
    for idx, (arr, expected) in enumerate(test_cases, 1):
        result = max_subarray(arr)
        assert result == expected, f"Test {idx} failed: expected {expected}, got {result}"
    print("All tests passed.")
