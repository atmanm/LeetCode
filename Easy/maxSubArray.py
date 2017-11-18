# Find the contiguous subarray within an array (containing at least one number)
# which has the largest sum.
#For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
#the contiguous subarray [4,-1,2,1] has the largest sum = 6.

class Solution(object):
    array = []
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#        if not nums:
#            return 0
#
#        maxSum = nums[0]
#        curSum = nums[0]
#
#        for num in nums[1:]:
#            curSum = max(num, curSum + num)
#            maxSum = max(maxSum, curSum)
#
#        return maxSum
        self.array = nums
        [curSum, maxSum] = self.findMaxSum(len(nums), nums[0])

        return maxSum

    def findMaxSum(self, maxIdx, maxSum):
        if maxIdx == 1:
            return [self.array[maxIdx-1],self.array[maxIdx-1]]

        [curSum, maxSum] = self.findMaxSum(maxIdx - 1, maxSum)

        curSum = max(curSum+self.array[maxIdx - 1], self.array[maxIdx - 1])
        maxSum = max(curSum, maxSum)

        return [curSum, maxSum]

if __name__ == "__main__":
    try:
        array = [int(x) for x in input().strip().split(',')]
    except ValueError:
        array = []

    print(Solution().maxSubArray(array))
