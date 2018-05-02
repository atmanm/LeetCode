#Given a collection of distinct numbers, return all possible permutations.

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        result = self.permuteHelper(nums, [], result)

        return result

    def permuteHelper(self, nums, curList, result):
        print(nums, curList, result)
        if len(nums) == 0:
            result.append(curList)
        for i in range(len(nums)):
            self.permuteHelper(nums[0:i]+nums[i+1:], curList+[nums[i]], result)

        return result

if __name__ == "__main__":
    nums = [int(x) for x in input().strip().split(',')]
    print(Solution().permute(nums))
