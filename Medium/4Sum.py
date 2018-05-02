#Given an array S of n integers, are there elements a, b, c, and d in S such
#that a + b + c + d = target? Find all unique quadruplets in the array which
#gives the sum of target.

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        retList = []

        nums = sorted(nums)
        i = 0
        while i < len(nums) - 3:
            while i < len(nums) - 3 and i > 0 and nums[i] == nums[i-1]:
                i += 1
            j = i + 1
            while j < len(nums) - 2:
                while j < len(nums) - 2 and j > i+1 and nums[j] == nums[j-1]:
                    j += 1

                lo = j+1
                hi = len(nums) - 1
                while lo < hi:
                    mySum = nums[lo] + nums[hi] + nums[i] + nums[j]
                    if mySum == target:
                        retList.append([nums[i], nums[j], nums[lo], nums[hi]])
                        while lo < len(nums)-1 and nums[lo] == nums[lo+1]:
                            lo += 1
                        while hi > 0 and nums[hi] == nums[hi-1]:
                            hi -= 1
                        lo += 1
                        hi -= 1
                    elif mySum < target:
                        lo += 1
                    else:
                        hi -= 1
                j += 1
            i += 1

        return retList

if __name__ == "__main__":
    nums = [int(x) for x in input().strip().split(',')]
    target = int(input().strip())

    print(Solution().fourSum(nums, target))
