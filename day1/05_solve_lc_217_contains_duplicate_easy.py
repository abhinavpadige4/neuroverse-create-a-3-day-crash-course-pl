'''day1/05_solve_lc_217_contains_duplicate_easy.py

Solution for LeetCode 217 – Contains Duplicate (Easy).
The problem statement:
    Given an integer array ``nums``, return ``True`` if any value appears
    at least twice in the array, and ``False`` otherwise.

Approach
--------
We use a ``set`` to keep track of numbers we have seen while iterating over the
array. If we encounter a number that is already in the set, we can immediately
return ``True``. If the loop finishes without finding a duplicate we return
``False``.

Complexity
----------
* Time: O(n) – one pass through the list.
* Space: O(n) – in the worst case we store every distinct element.

The implementation lives in ``solutions/0217_contains_duplicate.py``.  This
wrapper imports the core function and provides a simple command‑line interface
for quick manual testing.
''' 

from typing import List

# Import the core algorithm implementation.
from solutions.0217_contains_duplicate import contains_duplicate


def solve(nums: List[int]) -> bool:
    """Return ``True`` if ``nums`` contains any duplicate, else ``False``.

    This thin wrapper exists so that the file matches the repository's
    convention of exposing a ``solve`` function that can be called from the
    command line or unit tests.
    """
    return contains_duplicate(nums)


if __name__ == "__main__":
    # Simple manual test harness.
    import sys
    import json

    if len(sys.argv) != 2:
        print("Usage: python day1/05_solve_lc_217_contains_duplicate_easy.py '[1,2,3]'\n")
        sys.exit(1)

    try:
        # Expect a JSON‑encoded list as the sole argument.
        input_list = json.loads(sys.argv[1])
        if not isinstance(input_list, list):
            raise ValueError
    except Exception:
        print("Error: argument must be a JSON array, e.g. '[1,2,3]'\n")
        sys.exit(1)

    result = solve(input_list)
    print(result)
