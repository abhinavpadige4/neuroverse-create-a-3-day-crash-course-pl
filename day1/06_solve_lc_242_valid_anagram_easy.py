"""LeetCode 242 – Valid Anagram (Easy)

Problem statement
-----------------
Given two strings ``s`` and ``t``, return ``True`` if ``t`` is an anagram of ``s``, and ``False`` otherwise.

An *anagram* is a word or phrase formed by rearranging the letters of a different word or phrase,
using all the original letters exactly once.

Approach
--------
The most straightforward solution is to count the frequency of each character in both strings and
compare the two frequency maps.  Python's ``collections.Counter`` does exactly that, but to keep the
solution self‑contained and to demonstrate the underlying algorithm we implement the counting
manually using a dictionary.

Complexity
----------
* Time: ``O(n)`` where ``n`` is the length of the longer string – we iterate over each character once.
* Space: ``O(1)`` because the alphabet size is bounded (26 lowercase English letters in the original
  LeetCode constraints).  In a generic Unicode scenario the dictionary would grow with the number of
  distinct characters, which is still ``O(k)`` where ``k`` ≤ ``n``.

The implementation lives in ``solutions/0242_valid_anagram.py``.  This wrapper imports the function
and provides a tiny command‑line interface for quick manual testing.
"""

from typing import Dict

# Import the core solution implementation
from solutions.0242_valid_anagram import is_anagram


def main() -> None:
    """Simple interactive demo.

    Run the script and input two strings; the program prints whether they are anagrams.
    Example::

        $ python day1/06_solve_lc_242_valid_anagram_easy.py
        Enter first string: anagram
        Enter second string: nagaram
        Result: True
    """
    s = input("Enter first string: ").strip()
    t = input("Enter second string: ").strip()
    result = is_anagram(s, t)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
