# Given an array with n objects colored red, white or blue, sort them so that
# objects of the same color are adjacent, with the colors in the order red,
# white and blue.
#Here, we will use the integers 0, 1, and 2 to represent the color red, white,
#and blue respectively.

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify
        nums in-place instead.
        """

        forward = 0
        backward = len(nums) - 1
        skip = False

        while forward <= backward:
            if forward == backward:
                skip = True
            if nums[forward] == 0:
                nums.insert(0, nums.pop(forward))
                forward += 1
            elif nums[forward] == 2:
                nums.insert(len(nums) - 1, nums.pop(forward))
            else:
                forward += 1

            if skip:
                skip = False
                break

            if nums[backward] == 0:
                nums.insert(0, nums.pop(backward))
            elif nums[backward] == 2:
                nums.insert(len(nums) - 1, nums.pop(backward))
                backward -= 1
            else:
                backward -= 1


if __name__ == "__main__":
    nums = [int(x) for x in input().strip().split(',')]
    Solution().sortColors(nums)
    print(nums)
