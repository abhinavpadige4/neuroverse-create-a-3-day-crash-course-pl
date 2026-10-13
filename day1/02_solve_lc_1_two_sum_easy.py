'''\
LeetCode 1. Two Sum (Easy)
---------------------------
Given an integer array ``nums`` and an integer ``target``, return *indices* of the two numbers such that they add up to ``target``.
You may assume that each input would have **exactly one** solution, and you may not use the same element twice.
The answer can be returned in any order.

The classic optimal solution runs in O(n) time and O(n) extra space by using a hash map that stores
``value -> index`` for the elements we have already seen. While iterating we check whether ``target - nums[i]``
is already in the map – if it is, we have found the pair.

This script demonstrates the solution and provides a tiny command‑line test harness so that the file can be
executed directly (e.g. ``python -m day1/02_solve_lc_1_two_sum_easy.py``) or imported from the test suite.
'''\

from typing import List

# Import the core implementation from the shared ``solutions`` package.
# The relative import works because the repository root is added to ``PYTHONPATH`` when the tests run.
from solutions.0001_two_sum import two_sum


def solve(nums: List[int], target: int) -> List[int]:
    """Wrapper around the shared ``two_sum`` implementation.

    The wrapper exists so that the file follows the same public interface as the other
    ``dayX`` scripts in the repo (a ``solve`` function that receives the raw inputs and
    returns the answer).  Keeping the logic in ``solutions/0001_two_sum.py`` avoids code
    duplication and makes the unit‑tests easier to maintain.
    """
    return two_sum(nums, target)


if __name__ == "__main__":
    # Simple manual test – useful when running the file locally.
    example_nums = [2, 7, 11, 15]
    example_target = 9
    print("Input:", example_nums, "target:", example_target)
    print("Output indices:", solve(example_nums, example_target))
