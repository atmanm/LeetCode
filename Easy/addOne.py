#Given a non-negative integer represented as a non-empty array of digits, plus
#one to the integer.
#You may assume the integer do not contain any leading zero, except the number 0
#itself.
#The digits are stored such that the most significant digit is at the head of the
#list.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        newUnits = digits[-1] + 1
        carry = int(newUnits/10)
        digits[-1] = newUnits%10
        for idx in reversed(range(len(digits)-1)):
            newVal = digits[idx] + carry
            carry = int(newVal/10)
            digits[idx] = newVal%10

        if carry:
            digits.insert(0, carry)

        return digits


if __name__ == "__main__":
    try:
        array = [int(x) for x in input().strip().split(' ')]
    except ValueError:
        array = []

    print(Solution().plusOne(array))
