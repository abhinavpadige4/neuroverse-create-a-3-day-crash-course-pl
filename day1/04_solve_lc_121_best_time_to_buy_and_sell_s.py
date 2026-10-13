"""day1/04_solve_lc_121_best_time_to_buy_and_sell_s.py

LeetCode 121 – Best Time to Buy and Sell Stock (Easy)
-----------------------------------------------------

Problem statement
~~~~~~~~~~~~~~~~~
Given an array ``prices`` where ``prices[i]`` is the price of a given stock on day ``i``,
find the maximum profit you can achieve. You may complete **at most one** transaction
(i.e., buy one and sell one share of the stock). You cannot sell a stock before you buy
it.

The optimal solution runs in O(n) time and O(1) extra space by tracking the minimum
price seen so far and the best profit achievable at each step.

Implementation details
~~~~~~~~~~~~~~~~~~~~~~
* The core logic lives in :pyfunc:`solutions.0121_buy_sell_stock.max_profit`.
* This script provides a small command‑line interface for manual testing and also
  includes a simple ``unittest`` suite that validates the implementation against a
  handful of representative cases.
* The module can be executed directly: ``python -m day1.04_solve_lc_121_best_time_to_buy_and_sell_s``.

Usage example
~~~~~~~~~~~~~
>>> from day1.04_solve_lc_121_best_time_to_buy_and_sell_s import max_profit
>>> max_profit([7,1,5,3,6,4])
5
>>> max_profit([7,6,4,3,1])
0
"""

from __future__ import annotations

from typing import List

# Import the actual solution implementation from the shared ``solutions`` package.
# The path is fixed by the manifest and must match exactly.
from solutions.0121_buy_sell_stock import max_profit as _solution_max_profit


def max_profit(prices: List[int]) -> int:
    """Wrapper that forwards to the shared solution.

    The wrapper exists so that the file follows the same public API pattern as the
    other daily‑exercise scripts in the repository.

    Parameters
    ----------
    prices: List[int]
        List of daily stock prices.

    Returns
    -------
    int
        Maximum profit achievable with at most one transaction.
    """
    return _solution_max_profit(prices)


# ---------------------------------------------------------------------------
# Simple command‑line interface for quick manual checks.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import argparse
    import json
    import sys

    parser = argparse.ArgumentParser(
        description="Run LeetCode 121 – Best Time to Buy and Sell Stock solution"
    )
    parser.add_argument(
        "prices",
        type=str,
        help="JSON‑encoded list of integers, e.g. '[7,1,5,3,6,4]'",
    )
    args = parser.parse_args()
    try:
        price_list = json.loads(args.prices)
        if not isinstance(price_list, list) or not all(isinstance(x, int) for x in price_list):
            raise ValueError
    except Exception:
        sys.stderr.write("Error: 'prices' must be a JSON list of integers.\n")
        sys.exit(1)

    result = max_profit(price_list)
    print(result)


# ---------------------------------------------------------------------------
# Unit tests – kept lightweight to avoid external dependencies.
# ---------------------------------------------------------------------------
import unittest


class TestBestTimeToBuyAndSellStock(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(max_profit([7, 6, 4, 3, 1]), 0)
        self.assertEqual(max_profit([1, 2, 3, 4, 5]), 4)
        self.assertEqual(max_profit([5]), 0)
        self.assertEqual(max_profit([]), 0)

    def test_random(self):
        # monotonic decreasing should yield 0 profit
        self.assertEqual(max_profit([9, 8, 7, 6, 5, 4]), 0)
        # profit from last element being highest
        self.assertEqual(max_profit([3, 2, 6]), 4)


if __name__ == "__main__":
    # When the file is executed directly, run the unit tests after the CLI.
    # This mirrors the behaviour of other daily scripts in the repo.
    unittest.main(argv=[sys.argv[0]], exit=False)
