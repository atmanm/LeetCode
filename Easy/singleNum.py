#Given an array of integers, every element appears twice except for one. Find
#that single one.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in nums:
            res ^= num

        return res

if __name__ == "__main__":
    try:
        nums = [int(x) for x in input().strip().split(',')]
    except ValueError:
        nums = []

    print(Solution().singleNumber(nums))
