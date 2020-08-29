"""
Given an array of integers nums and and integer target, return the indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1]

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

"""


def twoSum(nums, target):

    # ####################### Brute Force Soln ###################
    # out = []
    # for x in range(0,len(nums)):
    #     u_t = target - nums[x]
    #     if u_t in nums[x+1 :]:
    #         out.append(x)
    #         ind = nums.index(u_t,x+1)
    #         out.append(ind)
    #         break
    # return out

    ##################### One - Pass Hash Map Soln ####################
    seen = {}
    for i, v in enumerate(nums):
        remaining = target - v
        if remaining in seen:
            return [seen[remaining], i]
        seen[v] = i
    return []

    # ###################### Two - Pass Hash Map Soln ####################
    # t = {}
    # for i, x in enumerate(nums):
    #     t[x] = i
    # for i, x in enumerate(nums):
    #     u_t = target - x
    #     if u_t in t and t[u_t] != i:
    #         return [i, t[u_t]]
    # return []
