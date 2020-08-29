"""

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""


def threeSum(nums):
    res = []

    # Sort given Array
    nums.sort()
    length = len(nums)

    # keep 1 element as fixed
    for i in range(length - 2):
        # Since we need total 3 elements we run loop till last but 2 elements only

        # Since array is sorted if we encounter a positive element no need not proceed for further
        # elements its of no use.
        if nums[i] > 0:
            break

        # If 2 consecutive elemets are same we get duplicates . So skipping the iteration
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # set left & right index for given fixed element
        l = i + 1
        r = length - 1

        # traverse through remaining elements to find other 2 elements to satisfy condition
        while l < r:
            total = nums[i] + nums[l] + nums[r]

            # If the sum is lesser than 0 decrement right index and move backward
            if total < 0:
                l += 1

            # If the sum is greater than 0 increment left index and move further
            elif total > 0:
                r -= 1

            # If the sum is 0 increment left index , move further also decrement right index ,move backward
            else:
                res.append([nums[i], nums[l], nums[r]])

                # If 2 consecutive elemets are same we for l & r we skip it and proceed further
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1

                l += 1
                r -= 1
    return res
