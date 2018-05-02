#Given a collection of numbers that might contain duplicates, return all
#possible unique permutations.

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()

        self.permuteHelper(nums, [], result)
        return result

    def permuteHelper(self, nums, curList, result):
        if not nums and curList not in result:
            result.append(curList)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.permuteHelper(nums[0:i]+nums[i+1:],
                               curList+[nums[i]],
                               result)


if __name__ == "__main__":
    nums = [int(x) for x in input().strip().split(',')]
    print(Solution().permuteUnique(nums))
