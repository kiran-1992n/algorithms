"""

Given a non-empty array of digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Example 3:
Input: digits = [0]
Output: [1]

Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9

"""


def plusOne(digits):
    
    # ################## Soltion-1 ####################
    # s = ""
    # for x in digits:
    #     s += str(x)
    # num = int(s)
    # r = num+1
    # a = [int(x) for x in str(r)]
    # return a

    #################### Soltion-2 ####################
    n = len(digits)
    res = [0 for x in range(n)]
    carry = 1
    j = n - 1
    while (j >= 0):
        if ((digits[j] + carry) > 9):
            res[j] = (digits[j] + carry) % 10
            carry = 1
        else:
            res[j] = (digits[j] + carry)
            carry = 0
        j -= 1
    if carry == 1:
        res.insert(0, 1)

    return res
