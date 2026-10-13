'''python
LeetCode 242 – Valid Anagram
================================
Given two strings ``s`` and ``t``, return ``True`` if ``t`` is an anagram of ``s``,
and ``False`` otherwise.

An *anagram* is a rearrangement of letters.  The classic solution is to compare the
frequency of each character in both strings.  If the counts match for every
character, the strings are anagrams.

Complexity
----------
* **Time** – ``O(n)`` where ``n`` is ``len(s) + len(t)``.  We traverse each string once.
* **Space** – ``O(1)`` because the alphabet size is bounded (26 lowercase letters
  for the typical LeetCode constraints).  We use a fixed‑size ``list`` of length 26
  or a ``defaultdict``; both are constant‑space with respect to input size.

Implementation Details
----------------------
* The function is named ``is_anagram`` to match the LeetCode signature.
* It first checks length equality – unequal lengths cannot be anagrams.
* A ``collections.Counter`` could be used, but a manual count with a list is
  faster and avoids the overhead of a hash table.
* The function is placed in ``solutions/0242_valid_anagram.py`` so that the
  repository's import structure works as expected.
''' 

from typing import List


def is_anagram(s: str, t: str) -> bool:
    """Return ``True`` if ``t`` is an anagram of ``s``.

    The implementation counts characters using a fixed‑size list for the
    lowercase English alphabet.  It works for any ASCII letters; for Unicode
    strings the logic can be extended by using ``collections.Counter``.
    """
    # Quick length check – differing lengths cannot be anagrams.
    if len(s) != len(t):
        return False

    # Assuming only lowercase English letters (LeetCode constraint).
    # ``counts[i]`` stores the net count of character ``chr(ord('a') + i)``.
    counts: List[int] = [0] * 26
    a_ord = ord('a')

    for ch_s, ch_t in zip(s, t):
        counts[ord(ch_s) - a_ord] += 1
        counts[ord(ch_t) - a_ord] -= 1

    # If all counts are zero, the strings are anagrams.
    return all(c == 0 for c in counts)


# ---------------------------------------------------------------------------
# Simple test harness – executed when the module is run directly.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("", "", True),
        ("a", "a", True),
        ("ab", "ba", True),
        ("ab", "abc", False),
    ]

    for s, t, expected in test_cases:
        result = is_anagram(s, t)
        assert result == expected, f"Failed for {s!r}, {t!r}: expected {expected}, got {result}"
    print("All tests passed.")
'''