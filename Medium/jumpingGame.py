# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
#Each element in the array represents your maximum jump length at that position.

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 1:
            return True

        maxIndex = 0
        for i,n in enumerate(nums):
            if i > maxIndex:
                return False
            maxIndex = max(maxIndex, i+n)
        return True

if __name__ == "__main__":
    nums = [int(x) for x in input().strip().split(',')]
    print(Solution().canJump(nums))
