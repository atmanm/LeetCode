#Given a collection of integers that might contain duplicates, nums, return all
#possible subsets (the power set).

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        resList = []

        nums.sort()
        self.subsetHelper(nums, resList, [])

        return resList

    def subsetHelper(self, nums, resList, curList):
        if curList not in resList:
            resList.append(curList)

        if len(nums) == 0:
            return

        for idx, num in enumerate(nums):
            self.subsetHelper(nums[idx+1:], resList, curList+[num])

if __name__ == "__main__":
    nums = [int(x) for x in input().strip().split(',')]

    print(Solution().subsetsWithDup(nums))
