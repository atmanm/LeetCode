#Given an array S of n integers, find three integers in S such that the sum is
#closest to a given number, target. Return the sum of the three integers. You may
#assume that each input would have exactly one solution.

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        closestSum = (2**32) - 1
        nums = sorted(nums)
        for i in range(len(nums)-2):
            lo = i+1
            hi = len(nums) - 1

            while lo < hi:
                mySum = nums[lo] + nums[hi] + nums[i]
                if mySum == target:
                    return mySum

                if abs(mySum - target) < abs(closestSum - target):
                    closestSum = mySum

                if target < mySum:
                    hi -= 1
                else:
                    lo += 1

        return closestSum

if __name__ == "__main__":
    nums = [int(x) for x in input().strip().split(',')]
    target = int(input().strip())

    print(Solution().threeSumClosest(nums, target))
