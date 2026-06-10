from __future__ import annotations

from typing import Iterable, Optional, Sequence, TypeVar

T = TypeVar("T")


def add(a: int, b: int) -> int:
    """
    Return the sum of two integers.
    """
    return a + b


def is_even(n: int) -> bool:
    """
    Return True if n is even, otherwise False.
    """
    return n % 2 == 0


def linear_search(nums: Sequence[T], target: T) -> Optional[int]:
    """
    Return the FIRST index where target appears in nums,
    or None if not found.
    """
    for i, value in enumerate(nums):
        if value == target:
            return i
    return None


def count_occurrences(items: Iterable[T], target: T) -> int:
    """
    Count how many times target appears in items.
    """
    count = 0
    for item in items:
        if item == target:
            count += 1
    return count


def last_index(nums: Sequence[T], target: T) -> Optional[int]:
    """
    Return the LAST index where target appears in nums,
    or None if not found.
    """
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == target:
            return i
    return None