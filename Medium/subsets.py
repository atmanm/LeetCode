#Given a set of distinct integers, nums, return all possible subsets (the power set).

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        resList = []
        self.subsetsHelper(nums, resList, [])

        return resList

    def subsetsHelper(self, nums, resList, curList):
        if curList not in resList:
            resList.append(curList)
        if len(nums) > 0:
            for idx, elem in enumerate(nums):
                self.subsetsHelper(nums[idx+1:], resList, curList+[elem])

if __name__ == "__main__":
    nums = [int(x) for x in input().strip().split(',')]

    print(Solution().subsets(nums))
