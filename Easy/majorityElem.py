#Given an array of size n, find the majority element. The majority element is
#the element that appears more than ⌊ n/2 ⌋ times.
#You may assume that the array is non-empty and the majority element always exist
#in the array.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numDict = {}
        length = len(nums)
        for num in nums:
            try:
                numDict[num] += 1
                if numDict[num] >= length/2:
                    return num
            except KeyError:
                numDict[num] = 1
                if numDict[num] >= length/2:
                    return num

if __name__ == "__main__":
    nums = [int(x) for x in input().strip().split(',')]
    print(Solution().majorityElement(nums))
