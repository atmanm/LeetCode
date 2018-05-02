# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
#If such arrangement is not possible, it must rearrange it as the lowest possible
#order (ie, sorted in ascending order).
#The replacement must be in-place, do not allocate extra memory.

# Eg: 0,1,2,5,3,3,0
#1. From right, keep going till you find an element less than previous (0,1,2,,5,,3,3,0)
#2. The element after this is pivot (0,1,,2,,5,3,3,0)
#3. Swap pivot with the rightmost element in the suffix greater than pivot (0,1,,3,,5,3,,2,,0)
#4. Reverse the suffix (0,1,3,,0,2,3,5)

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify
        nums in-place instead.
        """

        index = len(nums) - 1
        while index > 0 and nums[index] <= nums[index-1]:
            index -= 1

        if index == 0:
            nums = nums[::-1]
            return nums

        pivotIdx = index - 1

        index = len(nums) - 1
        while nums[index] <= nums[pivotIdx]:
            index -= 1

        tempVal = nums[index]
        nums[index] = nums[pivotIdx]
        nums[pivotIdx] = tempVal

        nums[pivotIdx+1:] = nums[:pivotIdx:-1]

        return nums

if __name__ == "__main__":
    nums = [int(x) for x in input().strip().split(',')]
    print(Solution().nextPermutation(nums))
