"""
LeetCode 217 - Contains Duplicate (Easy)

Given an integer array nums, return true if any value appears at least twice,
return false if every element is distinct.

Approach: Use a set to track seen values. If a value is already in the set,
return True immediately. Otherwise, add it to the set. If we finish the loop
without finding a duplicate, return False.

Time Complexity: O(n) - single pass through the array
Space Complexity: O(n) - set stores up to n unique values
"""


def contains_duplicate(nums: list[int]) -> bool:
    """
    Detect if any value appears at least twice in the array.

    Args:
        nums: A list of integers.

    Returns:
        True if any duplicate exists, False otherwise.
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def contains_duplicate_optimized(nums: list[int]) -> bool:
    """
    Alternative approach: compare length of set vs original array.
    If the set is smaller, there must be duplicates.

    Args:
        nums: A list of integers.

    Returns:
        True if any duplicate exists, False otherwise.
    """
    return len(set(nums)) != len(nums)


# --- Tests ---

def run_tests():
    """Run comprehensive test cases for contains_duplicate."""
    test_cases = [
        # (input, expected_output, description)
        ([1, 2, 3, 1], True, "Duplicate 1 at indices 0 and 3"),
        ([1, 2, 3, 4], False, "All elements distinct"),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True, "Multiple duplicates"),
        ([], False, "Empty array"),
        ([1], False, "Single element"),
        ([1, 1], True, "Two identical elements"),
        ([-1, -1], True, "Negative duplicates"),
        ([0, 0, 0], True, "All zeros"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], False, "All distinct 1-10"),
        ([100000, 100000], True, "Large duplicate values"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], False, "20 distinct elements"),
        ([5, 3, 8, 3, 9, 2, 7, 3], True, "Duplicate 3 appears three times"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20], True, "Last element is duplicate"),
    ]

    passed = 0
    failed = 0

    print("=" * 60)
    print("Running tests for contains_duplicate")
    print("=" * 60)

    for i, (nums, expected, description) in enumerate(test_cases, 1):
        result = contains_duplicate(nums)
        status = "PASS" if result == expected else "FAIL"
        if result == expected:
            passed += 1
        else:
            failed += 1
        print(f"Test {i:2d}: [{status}] {description}")
        print(f"        Input: {nums}")
        print(f"        Expected: {expected}, Got: {result}")
        print()

    # Test the optimized version too
    print("=" * 60)
    print("Running tests for contains_duplicate_optimized")
    print("=" * 60)

    for i, (nums, expected, description) in enumerate(test_cases, 1):
        result = contains_duplicate_optimized(nums)
        status = "PASS" if result == expected else "FAIL"
        if result == expected:
            passed += 1
        else:
            failed += 1
        print(f"Test {i:2d}: [{status}] {description}")
        print(f"        Input: {nums}")
        print(f"        Expected: {expected}, Got: {result}")
        print()

    print("=" * 60)
    print(f"Results: {passed} passed, {failed} failed out of {len(test_cases) * 2} tests")
    print("=" * 60)

    return failed == 0


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
