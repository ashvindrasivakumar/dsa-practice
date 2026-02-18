"""
Problem: Two Sum
Platform: LeetCode
Difficulty: Easy

Approach:
Use a hashmap (dictionary) to store visited numbers.
For each number, check if target - number exists in hashmap.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def two_sum(nums, target):
    lookup = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i

    return []


# Example run
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))

