'''day1/03_solve_lc_26_remove_duplicates_from_sorte.py

Solution for LeetCode 26 – Remove Duplicates from Sorted Array.
The implementation lives in ``solutions/0026_remove_duplicates.py`` and is
exposed via a ``Solution`` class with a ``removeDuplicates`` method.

This script imports the solution, runs a few sanity‑check test cases and
prints a short report.  It can be executed directly::

    python -m day1.03_solve_lc_26_remove_duplicates_from_sorte

The output is a simple ``PASS``/``FAIL`` table that is useful when the file
is run locally before committing to GitHub.
''' 

from typing import List

# Import the actual algorithm implementation
from solutions.0026_remove_duplicates import Solution as ImplSolution


def run_test(nums: List[int], expected_len: int, expected_nums: List[int]) -> bool:
    """Execute one test case.

    Parameters
    ----------
    nums: List[int]
        The input array (will be copied because the algorithm works in‑place).
    expected_len: int
        The length that ``removeDuplicates`` should return.
    expected_nums: List[int]
        The first ``expected_len`` elements of ``nums`` after the call.

    Returns
    -------
    bool
        ``True`` if both the returned length and the mutated array match the
        expectations, ``False`` otherwise.
    """
    # Work on a copy to keep the original test data intact for reporting
    arr = nums.copy()
    sol = ImplSolution()
    result_len = sol.removeDuplicates(arr)
    # Slice the array to the length reported by the algorithm
    result_arr = arr[:result_len]
    return result_len == expected_len and result_arr == expected_nums


def main() -> None:
    test_cases = [
        # (input array, expected length, expected first elements after dedup)
        ([1, 1, 2], 2, [1, 2]),
        ([0,0,1,1,1,2,2,3,3,4], 5, [0,1,2,3,4]),
        ([], 0, []),
        ([1], 1, [1]),
        ([1,1,1,1,1], 1, [1]),
    ]

    passed = 0
    for idx, (inp, exp_len, exp_arr) in enumerate(test_cases, 1):
        ok = run_test(inp, exp_len, exp_arr)
        status = "PASS" if ok else "FAIL"
        print(f"Test {idx}: {status}")
        if ok:
            passed += 1
    total = len(test_cases)
    print(f"\n{passed}/{total} tests passed.")


if __name__ == "__main__":
    main()
