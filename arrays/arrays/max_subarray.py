# Problem: Maximum Subarray
# Approach: Kadane's Algorithm
# Time: O(n) | Space: O(1)

def maxSubArray(nums):
    current = nums[0]
    maximum = nums[0]

    for i in range(1, len(nums)):
        current = max(nums[i], current + nums[i])
        maximum = max(maximum, current)

    return maximum

# Example
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
