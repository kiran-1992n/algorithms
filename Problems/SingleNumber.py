"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4

"""


def singleNumber(nums):

    # ##################Solution - 1 #######################
    # res = 0
    # for x in nums:
    #     res ^= x
    # return res

    # ##################Solution - 2 #######################
    t = {}
    for i, x in enumerate(nums):
        if x in t:
            del t[x]
        else:
            t[x] = i

    single_occurance_number = list(t.keys())[0]
    single_occurance_number_index = t[single_occurance_number]

    return single_occurance_number
