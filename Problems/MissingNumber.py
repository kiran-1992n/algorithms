"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:
Input: [3,0,1]
Output: 2

Example 2:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8

"""


def missingNumber(nums):
    n = len(nums)

    # Since we have '0' as 1 entry, we need to find sum of
    # first n natural numbers where n is array length.

    # If 0 was not part of aray formula is ((n+1)*(n+2)//2)
    required_sum = (n + 1) * (n) // 2

    s = sum(nums)
    return required_sum - s
