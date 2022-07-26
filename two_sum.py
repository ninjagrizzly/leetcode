# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    indexes = {}

    for idx, num in enumerate(nums):
        diff = target - num
        if diff in indexes:
            return [indexes[diff], idx]
        indexes[num] = idx


print(twoSum([1, 2, 3, 10, 4, 5, 6], 11))