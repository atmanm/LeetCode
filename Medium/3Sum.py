#Given an array S of n integers, are there elements a, b, c in S such that a + b
#+ c = 0? Find all unique triplets in the array which gives the sum of zero.

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        myList = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            mySum = 0 - nums[i]
            lo = i+1
            hi = len(nums) - 1
            while lo < hi:
                if nums[lo] + nums[hi] == mySum:
                    myList.append([nums[i], nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo+1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi-1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
                elif nums[lo] + nums[hi] < mySum:
                    lo += 1
                else:
                    hi -= 1

        return myList

if __name__ == "__main__":
    nums = [int(x) for x in input().strip().split(',')]
    print(Solution().threeSum(nums))
